from pygame import *
from win32api import GetSystemMetrics

W = GetSystemMetrics(0)
H = GetSystemMetrics(1)

win = display.set_mode((W,H),flags=FULLSCREEN)

font.init()

menu_font = font.SysFont("Impact", 42)



def set_640():
    global W,H
    W, H = 640, 480
    win = display.set_mode((W,H),flags=FULLSCREEN)

def set_1366():
    global W,H
    W = 1366
    H = 768   
    win = display.set_mode((W,H),flags=FULLSCREEN)
    
def set_1920():
    global W,H
    W = 1920
    H = 1080
    win = display.set_mode((W,H),flags=FULLSCREEN)

def set_2560():
    global W,H
    W = 2560
    H = 1440
    win = display.set_mode((W,H),flags=FULLSCREEN)



class Menu():
    def __init__(self,x,y, filename):
        self.image = image.load(filename)
        self.rect = Rect(x,y,500,600)

    def update(self):
        draw.rect(win,(77,77,77),self.rect)
        win.blit(self.image, self.rect)



class Button():
    def __init__(self,x,y, filename,func, mode = None):
        self.rect = Rect(x,y,200,100)
        self.func = func
        self.visible = True
        self.mode = mode
        self.filename = filename
        self.image = image.load(filename)
    
    def check_click(self,pos):
        if self.rect.collidepoint(pos) and self.visible is True: 
            if self.mode is None:
                self.func()
            else:
                self.func(self.mode)

    def update(self):
        if self.visible:
            draw.rect(win,(50,50,50),self.rect)
            win.blit(self.image, self.rect)
        


class ListButton():
    def __init__(self,x,y,filename,buttons, visible = False):
        self.rect = Rect(x,y,200,100)
        self.filename = filename
        self.image = image.load(filename)
        self.buttons = buttons
        self.visible = visible
        for btn in buttons:
            btn.visible = False
    
    def check_click(self,pos):
        if self.rect.collidepoint(pos): 
            if self.visible == False:
                self.show_buttons()
                self.visible = True
            elif self.visible == True:
                self.hide_buttons()
                self.visible = False

    def update(self):
        draw.rect(win,(50,50,50),self.rect)
        win.blit(self.image, self.rect)

    def show_buttons(self):
        for btn in self.buttons:
            btn.visible = True

    def hide_buttons(self):
        for btn in self.buttons:
            btn.visible = False



