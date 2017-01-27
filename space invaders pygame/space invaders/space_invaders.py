import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

white = (225,225,225)

crossImg = pygame.image.load("cross.png")
cx = 400
cy = 560

while True: # main game loop
    DISPLAY.fill(white)
    DISPLAY.blit(crossImg,(cx,cy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
