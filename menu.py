from pygame import *
#from win32api import GetSystemMetrics

W = 1920
H = 1080

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

class Menu():
    def __init__(self,x,y):
        self.rect = Rect(x,y,400,400)

    def update(self):
        draw.rect(win,(127,127,127),self.rect)

class Button():
    def __init__(self,x,y,text,func, mode = None):
        self.rect = Rect(x,y,200,100)
        self.text_pic = menu_font.render(text,True,(0,0,0))
        self.func = func
        self.visible = True
        self.mode = mode
    
    def check_click(self,pos):
        if self.rect.collidepoint(pos) and self.visible is True: 
            if self.mode is None:
                self.func()
            else:
                self.func(self.mode)

    def update(self):
        if self.visible:
            draw.rect(win,(50,50,50),self.rect)
            win.blit(self.text_pic, self.rect)
        

class ListButton():
    def __init__(self,x,y,text,buttons, visible = False):
        self.rect = Rect(x,y,200,100)
        self.text_pic = menu_font.render(text,True,(0,0,0))
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
        win.blit(self.text_pic, self.rect)

    def show_buttons(self):
        for btn in self.buttons:
            btn.visible = True

    def hide_buttons(self):
        for btn in self.buttons:
            btn.visible = False


