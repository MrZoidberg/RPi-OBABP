from time import sleep
import RPi.GPIO as GPIO


def main():
    led = 16
    button = 18
    pressed = False

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(led, GPIO.LOW)

    print("init done")

    while True:
        if GPIO.input(button) is False:
            sleep(0.01)
            if not pressed:
                print("button pressed")
                GPIO.output(led, GPIO.HIGH)
                pressed = True
        elif pressed:
            print("button released")
            GPIO.output(led, GPIO.LOW)
            pressed = False
        sleep(0.1)


if __name__ == '__main__':
    main()
