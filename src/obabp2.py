import os
import sys
import HWD

def main():
    hwd = None
    try:
        hwd = HWD()
        hwd.setStatusLed(18)
        hwd.setPowerLed(16)
        hwd.setPlayButton(11)
        hwd.setVolumeUpButton(13)
        hwd.setVolumeDownButton(15)
        hwd.setup()

        hwd.flashLed(hwd.powerLed, 2, 50)
        hwd.flashLed(hwd.statusLed, 2, 50)

        raw_input("Press Enter to exit...")
    except KeyboardInterrupt:
        print "exiting from button"
    except:
        print "Unexpected error:", sys.exc_info()[0]

    if hwd is not None:
        hwd.cleanup()
    # Restart application
    os.execl('runme.sh', '')

if __name__ == '__main__':
    main()
