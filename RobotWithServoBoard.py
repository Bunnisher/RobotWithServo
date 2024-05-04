from time import sleep
from machine import Pin, I2C
from machine import Pin, PWM
import time
import utime
from pca9685 import PCA9685
from servo import Servos


trigger = Pin(11, Pin.OUT)
echo = Pin(10, Pin.IN)

In1=Pin(6,Pin.OUT) 
In2=Pin(7,Pin.OUT)  
EN_A=Pin(8,Pin.OUT)



#OUT3  and OUT4
In3=Pin(4,Pin.OUT)  
In4=Pin(3,Pin.OUT)  
EN_B=Pin(2,Pin.OUT)

EN_A.high()
EN_B.high()

sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)
servo.position(index=0, degrees=180)
servo.position(index=1, degrees=180)
servo.position(index=2, degrees=180)
servo.position(index=3, degrees=180)


def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    
#Turn Right
def turn_right():
    In1.low()
    In2.low()
    In3.low()
    In4.high()
    
#Turn Left
def turn_left():
    In1.low()
    In2.high()
    In3.low()
    In4.low()
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    

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
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   #oled.fill(0)
   distance2 = str(distance)
   if distance < 20.0:
       print("Shit is too close")
       #oled.text("Distance:  ", 0, 0)
       distance2 = str(distance)
       servo.position(index=0, degrees=20)
       servo.position(index=1, degrees=180)
       servo.position(index=2, degrees=180)
       servo.position(index=3, degrees=180)
       time.sleep(2)
       servo.position(index=0, degrees=50)
       servo.position(index=1, degrees=0)
       servo.position(index=2, degrees=0)
       servo.position(index=3, degrees=50)
       time.sleep(2)
       servo.position(index=0, degrees=75)
       servo.position(index=1, degrees=75)
       servo.position(index=2, degrees=75)
       servo.position(index=3, degrees=75)
       time.sleep(2)
       servo.position(index=0, degrees=180)
       servo.position(index=1, degrees=180)
       servo.position(index=2, degrees=180)
       servo.position(index=3, degrees=180)
       time.sleep(2)
       
while True:
    ultra()
    utime.sleep(.08)
    move_forward()
    print("Forward")
    utime.sleep(2)
    stop()
    print("Stop")
    utime.sleep(2)
    move_backward()
    print("Backward")   
    utime.sleep(2)
    stop()
    print("Stop")
    utime.sleep(2)
        
        