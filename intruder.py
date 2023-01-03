from machine import Pin, Timer
import utime
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
    
while True:
    print("test")
    ultra()
    utime.sleep(.5)
##if test doesnt print, loop is broken
     

led = Pin(15, Pin.OUT)
timer = Timer()
    
def blink(timer):
    led.toggle()
        
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
    
