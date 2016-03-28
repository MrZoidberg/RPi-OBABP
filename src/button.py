from time import sleep
import RPi.GPIO as GPIO


def main():
    led = 16
    button = 11
    pressed = False

    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)

    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print("init done")
    try:
        while True:
            if GPIO.input(button) is False:
                sleep(0.01)
                if not pressed:
                    print("button pressed")
                    GPIO.output(led, GPIO.LOW)
                    pressed = True
            elif pressed:
                print("button released")
                GPIO.output(led, GPIO.HIGH)
                pressed = False
            sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
