from pygame import *
#from win32api import GetSystemMetrics

bg = image.load("background.png")

W = 1920
H = 1080

coficent = (W*H)/(2560*1440)

win = display.set_mode((W,H),flags=FULLSCREEN)

font.init()

menu_font = font.SysFont("Impact", 42)

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
    def __init__(self,x,y, filename):
        self.image = image.load(filename)
        self.rect = Rect(x,y,500,600)

    def update(self):
        win.blit(self.image, self.rect)



class Button():
    def __init__(self,x,y, text, func, mode = None):
        self.x = x
        self.y = y
        self.rect = Rect(self.x,self.y,200,100)
        self.func = func
        self.visible = True
        self.mode = mode
        self.text_pic = menu_font.render(text,True,(0,0,0))
        self.image = image.load("button.png")
        self.image = transform.scale(self.image, (200,100))
    
    def check_click(self,pos):
        if self.rect.collidepoint(pos) and self.visible is True: 
            if self.mode is None:
                self.func()
            else:
                self.func(self.mode)

    def update(self):
        if self.visible:
            win.blit(self.image, self.rect)
            win.blit(self.text_pic, (self.x, self.y))
        


class ListButton():
    def __init__(self,x,y,text,buttons, visible = False):
        self.rect = Rect(x,y,200,100)
        self.text_pic = menu_font.render(text,True,(0,0,0))
        self.image = image.load("button.png")
        self.image = transform.scale(self.image, (200,100))
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
        win.blit(self.image, self.rect)
        win.blit(self.text_pic, self.rect)

    def show_buttons(self):
        for btn in self.buttons:
            btn.visible = True

    def hide_buttons(self):
        for btn in self.buttons:
            btn.visible = False



