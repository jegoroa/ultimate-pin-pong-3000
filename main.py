from pygame import *

class Mychik():
    def __init__(self,x,y,w,h,speed,filename,vface,hface):
        self.speed = speed
        self.filename = filename
        self.rect = Rect(x,y,w,h)
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (w,h))
        self.rect.x = x
        self.rect.y = y
        self.vface = vface
        self.hface = hface

    def reset(self):
        win.blit( self.image , (self.rect.x, self.rect.y) )

    def update(self):
        if self.hface == "right":
            self.rect.x += self.speed
            if self.rect.x > w:
                self.hface = "left"

        if self.hface == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.hface = "right"
        
        if self.vface == "up":
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.vface = "dawn"

        if self.vface == "dawn":
            self.rect.y += self.speed
            if self.rect.y > h:
                self.vface = "up"

        self.reset()

ball = Mychik(100,100,40,40,1,'beach-ball-icon.png','up','right' )

lightgreen = (0,255,100)

win = display.set_mode((1000,500))
w = 1000
h = 500

while True:

    for e in event.get():
        if e.type == QUIT:
            exit()

    win.fill(lightgreen)
    ball.update()
    display.update()