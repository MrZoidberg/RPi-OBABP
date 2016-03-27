'''
Created on Nov 21, 2012

@author: proteus
'''
from vonProteus.RPi.OBABP.OBABP import OBABP
import RPi.GPIO as GPIO


def main():
    obabp = OBABP()
    obabp.setLed(18)
    obabp.setButton(11)
    obabp.setDriveName("AUDIO")
    obabp.setMountPoint("/mnt/usb/")
    obabp.setMusicDir("/var/lib/mpd/music/")
    obabp.setMpdTagCasche("/var/lib/mpd/tag_cache")
    obabp.satupGPIO(GPIO.BOARD)
    obabp.go()

if __name__ == '__main__':
    main()
