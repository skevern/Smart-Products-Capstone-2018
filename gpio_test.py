from gpiozero import LED
from time import sleep

speed1 = LED(13)
speed2 = LED(19)
speed3 = LED(26)
speed4 = LED(12)
pump1 = LED(16)
pump2 = LED(21)
#servo = 17


speed1.on()
sleep(0.50)
speed1.off()
sleep(2)

speed2.on()
sleep(0.50)
speed2.off()
sleep(2)

speed3.on()
sleep(0.50)
speed3.off()
sleep(2)

speed4.on()
sleep(0.50)
speed4.off()

    
    