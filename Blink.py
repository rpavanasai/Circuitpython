import board, time
import digitalio

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)