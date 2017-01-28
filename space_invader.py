import pygame, sys
from pygame.locals import *
pygame.init()

class invader:# Class for object
    def __init__(cx,spriteLength,width):
        self.cx = cx
        self.spriteLength = spriteLength
        self.width = width

    def move_right(self,cx,spriteLength,width):# invader turns right
        if self.cx == self.width-self.spriteLength:# boundaries
            print("outside boundary limits")
            self.cx=self.cx-5
        self.cx=self.cx+5
        return self.cx
    def move_left(self,cx,spriteLength,width):# invader turns left
        if cx == 0:# boundaries
            print("outside boundary limits")
            self.cx=self.cx+5
        self.cx=self.cx-5
        return self.cx
