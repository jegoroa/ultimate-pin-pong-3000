from pygame import *


lightgreen = (0,255,100)

win = display.set_mode((1000,500))

class PlatForm():
    def __init__(self,x,y,width,height,speed,pic_name):
        self.pic = image.load(pic_name)
        self.rect = Rect(x,y,width,height)
        self.speed = speed

    def update(self):
        if self.ymove == 'down':
            self.rect.y += self.speed
            if self.rect.y > 400:
                self.rect.y = 400
        else:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
                
        self.reset()


    def reset(self):
        win.blit(self.pic,( self.rect.x,self.rect.y))

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
        
platform = PlatForm(x=100,y=350,width=50,height=150,speed=1,pic_name="platform.png")
platform.ymove = "-"

platform1 = PlatForm(x=800,y=350,width=50,height=150,speed=1,pic_name="platform.png")
platform1.ymove = "-"

ball = Mychik(100,100,40,40,1,'beach-ball-icon.png','up','right' )

lightgreen = (0,255,100)

win = display.set_mode((1000,500))
w = 1000
h = 500

    
while True:

    
    for e in event.get():
        if e.type == QUIT:
            exit()
        
        if e.type == KEYDOWN:
            if e.key == K_w:
                platform.ymove = "up"

            if e.key == K_s:
                platform.ymove = "down"

            if e.key == K_UP:
                platform1.ymove = "up"

            if e.key == K_DOWN:
                platform1.ymove = "down"


    
    
    win.fill(lightgreen)
    ball.update()
    platform.update()
    platform1.update()
    display.update()