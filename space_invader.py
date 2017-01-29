class invader():# Class for object
    def __init__(self):
        self.cx = cx
        self.boundaryRight = boundaryRight
    def move_right(self,cx,boundaryRight):# invader turns right
        if self.cx == self.boundaryRight:# boundaries
            print("outside boundary limits")
            self.cx=self.cx-5
        self.cx=self.cx+5
        return self.cx
    def move_left(self,cx):# invader turns left
        if self.cx == 0:# boundaries
            print("outside boundary limits")
            self.cx=self.cx+5
        self.cx=self.cx-5
        return self.cx
