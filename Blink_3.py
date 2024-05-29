import board, time, digitalio, microcontroller

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

interval = 0.5
last_blink_time = time.monotonic() 

while True:
    current_time = time.monotonic() 
    if current_time-last_blink_time >= interval:
        led.value = not led.value
        last_blink_time = current_time
    