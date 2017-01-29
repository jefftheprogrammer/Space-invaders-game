# IMPORTS
import pygame, sys
from pygame.locals import *
from space_invader import invader
pygame.init()
###################
#IMAGE SIZE AND FPS
width = 800
height = 600
fps = 30
fpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((width,height))

#OTHER VARIABLES
pygame.display.set_caption('space invaders!')
white = (225,225,225)# The colour white
crossImg = pygame.image.load("cross.png")# The invader image is stored in the crossImg variable
spriteLength = 40
cx = 400
cy = 560
boundaryRight = width-spriteLength
keypress = ""
invader = invader(cx,boundaryRight)

while True: # main game loop
    DISPLAY.fill(white)
    DISPLAY.blit(crossImg,(cx,cy))
    keypress = pygame.key.get_pressed()# finds what key the user is pressing
    #print(cx,cy)# debugging

    if keypress[K_RIGHT]:# right
        cx = invader.move_right(cx,boundaryRight)# Calls a function from another file
    elif keypress[K_LEFT]:# left
        cx = invader.move_left(cx)# Calls a function from another file

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)
