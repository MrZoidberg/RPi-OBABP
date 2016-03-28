import os
import traceback
from GPIOHWD import GPIOHWD


def main():
    hwd = None
    print ("====> Audio player start")

    try:
        hwd = GPIOHWD()
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
    except Exception:
        traceback.print_exc()

    if hwd is not None:
        hwd.cleanup()
    # Restart application

if __name__ == '__main__':
    main()
