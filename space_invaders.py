import pygame, sys
from pygame.locals import *
pygame.init()

width = 800
height = 600

fps = 30
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((width,height))
pygame.display.set_caption('space invaders!')

white = (225,225,225)

crossImg = pygame.image.load("cross.png")
cx = 400
cy = 560

keypress = ""

while True: # main game loop
    DISPLAY.fill(white)
    DISPLAY.blit(crossImg,(cx,cy))
    keypress = pygame.key.get_pressed()# finds what key the user is pressing

    if keypress[K_RIGHT]:
        cx=cx+5
        if cx == width-40:# boundaries
            print("outside boudary limits")
            cx=cx+5
    elif keypress[K_LEFT]:
        if cx == 0:# boundaries
            print("outside boudary limits")
            cx=cx+5
        cx=cx-5
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)
