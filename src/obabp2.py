import os
import traceback
import HWD

def main():
    hwd = None
    print ("====> Audio player start")

    try:
        hwd = HWD()
        hwd.setStatusLed(18)
        hwd.setPowerLed(16)
        hwd.setPlayButton(11)
        hwd.setVolumeUpButton(13)
        hwd.setVolumeDownButton(15)
        hwd.setup()

        print ("setup complete")

        hwd.flashLed(hwd.powerLed, 2, 50)
        hwd.flashLed(hwd.statusLed, 2, 50)

        raw_input("Press Enter to exit...")
    except KeyboardInterrupt:
        print "exiting from button"
    except Exception, e:
        print str(e)
        traceback.print_exc()

    if hwd is not None:
        hwd.cleanup()
    # Restart application

if __name__ == '__main__':
    main()
