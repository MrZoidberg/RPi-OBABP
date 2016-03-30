import os
import traceback
import time
from GPIOHWD import GPIOHWD
from player import Player
import pyudev


def checkForUSBDevice(driveName):
    res = ""
    context = pyudev.Context()
    try:
        for device in context.list_devices(subsystem='block',
                                           DEVTYPE='partition'):
            if device.get('ID_FS_LABEL') == driveName:
                    res = device.device_node
        return res
    except DeviceNotFoundAtPathError:
        return res


def loadMusic(device, mountPoint, musicDir, tagCacheDir):
    os.system("mount "+device+" "+mountPoint)
    os.system("/etc/init.d/mpd stop")
    os.system("rm -rf "+musicDir+"*")
    os.system("cp "+mountPoint+"* "+musicDir)
    os.system("umount "+mountPoint)
    os.system("rm "+tagCacheDir)
    os.system("/etc/init.d/mpd start")
    os.system("mpc clear")
    os.system("mpc ls | mpc add")
    os.system("/etc/init.d/mpd restart")


def main():
    hwd = None
    driveName = 'AUDIO'
    print ("====> Audio player start")

    try:
        hwd = GPIOHWD()
        hwd.setStatusLed(18)
        hwd.setPowerLed(16)
        hwd.setPlayButton(11)
        hwd.setVolumeUpButton(13)
        hwd.setVolumeDownButton(15)
        hwd.setup()

        hwd.flashLed(hwd.powerLed, 1, 1)
        hwd.flashLed(hwd.statusLed, 1, 1)

        print ("hardware setup complete")

        time.sleep(1)

        player = Player()
        player.setPort('6600')
        player.setHost('localhost')
        player.connectMPD()

        hwd.stopFlash(hwd.powerLed)
        hwd.updateLed(hwd.powerLed, True)
        hwd.stopFlash(hwd.statusLed)

        while(True):
            pendrive = checkForUSBDevice(driveName)

            if pendrive != "":
                print "new music detected"
                hwd.flashLed(hwd.statusLed, 2, 1)

                player.disconnect()
                loadMusic(pendrive, "/mnt/usb/", "/var/lib/mpd/music/",
                                    "/var/lib/mpd/tag_cache")
                player.connectMPD()
                print "new music added"
                hwd.flashLed(hwd.statusLed, 3, 1)
                while checkForUSBDevice() == pendrive:
                    time.sleep(0.1)
                print "usb drive removed"
                hwd.stopFlash(hwd.statusLed)

            time.sleep(0.1)

        raw_input("Press Enter to exit...")
    except KeyboardInterrupt:
        print "exiting from button"
    except Exception:
        traceback.print_exc()

    hwd.cleanup()
    # Restart application

if __name__ == '__main__':
    main()
