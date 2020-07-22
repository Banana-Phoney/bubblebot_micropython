import machine
import time


servp = machine.Pin(4)
servo = machine.PWM(servp, freq=50)
relay = machine.Pin(16, machine.Pin.OUT)

wand = 40

while True:
    wand = 40
    servo.duty(wand)
    time.sleep_ms(200)
    for i in range(47):
        servo.duty(wand)
        print(wand)
        wand +=1
        time.sleep_ms(25)
    time.sleep_ms(200)
    relay.value(1)
    time.sleep(2)
    relay.value(0)
    time.sleep(1)
