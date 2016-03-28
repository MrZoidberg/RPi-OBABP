import RPi.GPIO as GPIO


class GPIOHWD(object):

    def __init__(self,):
        print("GPIO version: " + GPIO.VERSION)
        GPIO.setmode(GPIO.BOARD)
        self._statusLed = -1
        self._powerLed = -1
        self._playButton = -1
        self._volumeUpButton = -1
        self._volumeDownButton = -1
        self.flashes = dict()

    @property
    def statusLed(self):
        return self._statusLed

    @property
    def powerLed(self):
        return self._powerLed

    @property
    def playButton(self):
        return self._playButton

    @property
    def volumeUpButton(self):
        return self._volumeUpButton

    @property
    def volumeDownButton(self):
        return self._volumeDownButton

    def setStatusLed(self, _led):
        self._statusLed = _led

    def setPowerLed(self, _led):
        self._powerLed = _led

    def setPlayButton(self, _button):
        self._playButton = _button

    def setVolumeDownButton(self, _button):
        self._volumeDownButton = _button

    def setVolumeUpButton(self, _button):
        self._volumeUpButton = _button

    def flashLed(self, led, speed, time):
        print("flashing led " + str(led) + " at freq " + str(speed) +
              " with duty " + str(time))
        pwm = GPIO.PWM(led, speed)
        pwm.start(time)
        self.flashes[led] = pwm

    def stopFlash(self, led):
        print("stop flashing led " + str(led))
        pwm = self.flashes[led]
        if pwm is not None:
            pwm.stop()
            del self.flashes[led]

    def setup(self):
        leds = [self._powerLed, self._statusLed]
        buttons = [self._playButton, self._volumeUpButton,
                   self._volumeDownButton]

        GPIO.setup(leds, GPIO.OUT)
        GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.output(self._powerLed, GPIO.HIGH)
        GPIO.output(self._statusLed, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()
