from sense_hat import SenseHat
import time
sense = SenseHat()

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

image1 = [
e,e,e,e,e,e,e,e,
e,y,y,y,y,y,y,e,
e,e,y,b,b,y,e,e,
e,e,y,b,b,y,e,e,
e,e,e,y,y,e,e,e,
e,e,y,e,e,y,e,e,
e,e,y,e,e,y,e,e,
e,y,y,y,y,y,y,e
]

image2 = [
e,e,e,e,e,e,e,e,
e,y,y,y,y,y,y,e,
e,e,y,e,b,y,e,e,
e,e,y,b,b,y,e,e,
e,e,e,y,y,e,e,e,
e,e,y,e,e,y,e,e,
e,e,y,b,e,y,e,e,
e,y,y,y,y,y,y,e
]

image3 = [
e,e,e,e,e,e,e,e,
e,y,y,y,y,y,y,e,
e,e,y,e,e,y,e,e,
e,e,y,b,b,y,e,e,
e,e,e,y,y,e,e,e,
e,e,y,e,e,y,e,e,
e,e,y,b,b,y,e,e,
e,y,y,y,y,y,y,e
]

image4 = [
e,e,e,e,e,e,e,e,
e,y,y,y,y,y,y,e,
e,e,y,e,e,y,e,e,
e,e,y,e,b,y,e,e,
e,e,e,y,y,e,e,e,
e,e,y,b,e,y,e,e,
e,e,y,b,b,y,e,e,
e,y,y,y,y,y,y,e
]

image5 = [
e,e,e,e,e,e,e,e,
e,y,y,y,y,y,y,e,
e,e,y,e,e,y,e,e,
e,e,y,e,e,y,e,e,
e,e,e,y,y,e,e,e,
e,e,y,b,b,y,e,e,
e,e,y,b,b,y,e,e,
e,y,y,y,y,y,y,e
]


sense.set_pixels(image1)
time.sleep(2)
sense.set_pixels(image2)
time.sleep(2)
sense.set_pixels(image3)
time.sleep(2)
sense.set_pixels(image4)
time.sleep(2)
sense.set_pixels(image5)

sense.set_rotation(90)
time.sleep(0.5)
sense.set_rotation(180)
time.sleep(0.5)
sense.set_rotation(270)
time.sleep(0.5)
sense.set_rotation(180)
time.sleep(0.5)

sense.set_pixels(image4)
time.sleep(2)
sense.set_pixels(image3)
time.sleep(2)
sense.set_pixels(image2)
time.sleep(2)
sense.set_pixels(image1)
time.sleep(2)

sense.set_rotation(90)
time.sleep(0.5)
sense.set_rotation(180)
time.sleep(0.5)
sense.set_rotation(270)
time.sleep(0.5)
sense.set_rotation(0)
time.sleep(0.5)

sense.set_pixels(image1)
time.sleep(2)
sense.set_pixels(image2)
time.sleep(2)
sense.set_pixels(image3)
time.sleep(2)
sense.set_pixels(image4)
time.sleep(2)
sense.set_pixels(image5)
