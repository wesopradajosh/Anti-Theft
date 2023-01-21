from pushbullet import Pushbullet
from machine import Pin, PWM
import utime
from utime import sleep
buzzer = PWM(Pin(15))
pb = Pushbullet ("o.EB4goltRmC8hcyJUd5m3kTsW9HeEj0Vv")
print(pb.devices)
buzzer.freq(500)
buzzer.duty_u16(1000)
sleep(1)
buzzer.duty_u16(0)

# If buzz doesnt play, code is broken

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = ((timepassed * 0.0343) / 2)
    print(distance)
    while distance < 20:
        buzzer.duty_u16(1000)
        sleep(1)
        buzzer.duty_u16(0)
        print("INTRUDER DETECTED")
        dev = pb.get_device('Google Coral')
        push = dev.push_note("Alert", "Movement Detected!")
        sleep(1)
     
        
## All of its functions

    
while True:
    print("Scanning")
    ultra()
    utime.sleep(.01)
## If "Scanning" doesnt print, loop is broken
 
 

    