import board, time
import digitalio

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = True
while True:
    led.value = not led.value
    time.sleep(2)
