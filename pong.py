from pygame import *

#from win32api import GetSystemMetrics


def set_640():
    global W,H, bg
    W, H = 640, 480
    bg = transform.scale(bg , (W, H))
    win = display.set_mode((W,H),flags=FULLSCREEN)

def set_1366():
    global W,H, bg
    W = 1366
    H = 768
    bg = transform.scale(bg , (W, H))
    win = display.set_mode((W,H),flags=FULLSCREEN)
    
def set_1920():
    global W,H, bg
    W = 1920
    H = 1080
    bg = transform.scale(bg , (W, H))
    win = display.set_mode((W,H),flags=FULLSCREEN)

def set_2560():
    global W,H, bg
    W = 2560
    H = 1440
    bg = transform.scale(bg , (W, H))
    win = display.set_mode((W,H),flags=FULLSCREEN)

class Menu():
    def __init__(self,x,y, filename,win):
        self.image = image.load(filename)
        self.rect = Rect(x,y,500,600)
        self.win = win

    def update(self):
        self.win.blit(self.image, self.rect)

class Button():
    def __init__(self,x,y, text, func,win, mode = None, w = 200):
        self.x = x
        self.y = y
        self.rect = Rect(self.x,self.y,w,100)
        self.func = func
        self.visible = True
        self.mode = mode
        self.image = image.load(text)
        self.image = transform.scale(self.image, (w,100))
        self.win=win

    def check_click(self,pos):
        if self.rect.collidepoint(pos) and self.visible is True: 
            if self.mode is None:
                print (self.func)
                self.func()
            else:
                self.func(self.mode)

    def update(self):
        if self.visible:
            self.win.blit(self.image, self.rect)

class ListButton():
    def __init__(self,x,y,text,buttons,win, visible = False):
        self.rect = Rect(x,y,200,100)
        self.image = image.load(text)
        self.image = transform.scale(self.image, (200,100))
        self.buttons = buttons
        self.visible = visible
        for btn in buttons:
            btn.visible = False
        self.win=win
    
    def check_click(self,pos):
        if self.rect.collidepoint(pos): 
            if self.visible == False:
                self.show_buttons()
                self.visible = True
            elif self.visible == True:
                self.hide_buttons()
                self.visible = False

    def update(self):
        self.win.blit(self.image, self.rect)

    def show_buttons(self):
        for btn in self.buttons:
            btn.visible = True

    def hide_buttons(self):
        for btn in self.buttons:
            btn.visible = False

class Picture():
    def __init__(self,x,y, w, h, text,win):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, w, h)
        self.visible = True
        self.image = image.load(text)
        self.image = transform.scale(self.image, (w,h))
        self.win=win

    def update(self):
        if self.visible:
            self.win.blit(self.image, self.rect)

