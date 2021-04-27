from machine import Pin
import time

p5 = Pin(14, Pin.OUT)
p2 = Pin(2, Pin.OUT)

#def toggle(max):# max 5
#lap = 0
#m = max

while True:
#while(lap <= 10):    
    p5.value(1)
    p2.value(0)
    time.sleep(0.8)
    p5.value(0)
    p2.value(1)
    time.sleep(1)
    #lap += 1
    #print(lap,'\n')
#toggle(10)      
#toggle(3)          