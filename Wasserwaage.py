from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
import math

pygame.init()
pygame.display.set_mode((1, 1))

sense = SenseHat()

white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

sense.clear()
sense.set_pixel(5, 5, white)
sense.set_pixel(2, 5, green)
sense.set_pixel(2, 3, yellow)
sense.set_pixel(2, 1, red)

y = 5

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            sense.set_pixel(5, y, 0, 0, 0)
            if event.key == K_DOWN and y < 5:
                y += 2
            elif event.key == K_UP and y > 1:
                y -= 2
            sense.set_pixel(5, y, 255, 255, 255)
            if event.key == K_RETURN and y == 1:
                toleranz = 0.5
            if event.key == K_RETURN and y == 3:
                toleranz = 0.3
            if event.key == K_RETURN and y == 5:
                toleranz = 0.1



accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))


print(accel_only["pitch"])

#LR = math.tan(x)) * 100
#OU = math.tan(y) * 100


#print({pitch})

#print type ()
