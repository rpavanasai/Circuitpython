import time, microcontroller

while True:
    cpu_temp = microcontroller.cpu.temperature
    print(cpu_temp,"'C")
    print(cpu_temp*(9/5)+32,"'F" )
    time.sleep(2)
