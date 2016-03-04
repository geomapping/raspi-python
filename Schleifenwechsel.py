from sense_hat import SenseHat
import pygame
from pygame.locals import *
from time import sleep

pygame.init()
pygame.display.set_mode((1,1))
sense = SenseHat()
loop = True
i = 0

while i < 25:

    i += 1
    
    while loop == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    loop = False
        print("1")
        sleep(1)
        
    while loop == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    loop = True
        print("2")
        sleep(1)

