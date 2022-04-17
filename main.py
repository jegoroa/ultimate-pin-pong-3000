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

platform = PlatForm(x=100,y=350,width=50,height=150,speed=1,pic_name="platform.png")
platform.ymove = "-"

platform1 = PlatForm(x=800,y=350,width=50,height=150,speed=1,pic_name="platform.png")
platform1.ymove = "-"



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
    platform.update()
    platform1.update()
    display.update()