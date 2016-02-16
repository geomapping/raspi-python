from sense_hat import SenseHat
import time
import random

sense = SenseHat()

sense.show_message("Hallo", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
sense.show_letter("F",text_colour=[255, 0, 0])
time.sleep(1)
sense.show_letter("+",text_colour=[0, 255, 0])
time.sleep(1)
sense.show_letter("M",text_colour=[0, 0, 255])
time.sleep(1)


a=0
while a<3:
    a=a+1
    z = random.randint(0,255)
    y = random.randint(0,255)
    x = random.randint(0,255)
    sense.show_message("Bunt", scroll_speed=0.05, text_colour=[z,y,x])
sense.set_pixel(1,1, [255, 0, 0])
sense.set_pixel(6,6, [0, 0, 255])
time.sleep(1)


r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
image = [
r,g,g,r,r,g,g,r,
r,b,b,b,b,b,b,b,
g,g,r,r,b,g,g,r,
r,g,g,r,b,r,g,g,
r,r,g,g,b,r,r,g,
g,r,r,g,b,g,r,r,
g,r,g,r,b,r,g,r,
r,g,g,r,r,g,g,r,
]
sense.set_pixels(image)
sense.set_rotation(90)
time.sleep(1)


sense.show_letter("Z")
angles = [0,90,180,270,0,90,180,270]
for r in angles:
    sense.set_rotation(r)
    time.sleep(1)

r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
image = [
r,g,g,r,r,g,g,r,
r,b,b,b,b,b,b,b,
g,g,r,r,b,g,g,r,
r,g,g,r,b,r,g,g,
r,r,g,g,b,r,r,g,
g,r,r,g,b,g,r,r,
g,r,g,r,b,r,g,r,
r,g,g,r,r,g,g,r,
]
sense.set_pixels(image)
v = 0
while v<4:
    time.sleep(1)
    v = v + 1
    sense.flip_v()

sense.clear(255,0,0)
