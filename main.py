from pygame import *
from menu import *

mode = "start_screen"

def start():
    global mode
    mode = "game"

def setting():
    global mode
    mode = "setting"

def menu():
    global mode
    mode = "start_screen"

lightgreen = (0,255,100)



#start_screen
start_menu = Menu(W/2-100,300)
start_btn = Button(W/2-100,400,"Start", start)
settings_btn = Button(W/2-100,500, "Settings", setting)
exit_btn = Button(W/2-100,600,"Exit", exit)

#setting
btn1920 = Button(W/2-100,400,"1920x1080",set_1920)
btn1366 = Button(W/2-100,500,"1366x768",set_1366)
btn640 = Button(W/2-100,600,"640x480", set_640)

res_list = ListButton(W/2-100,300,(str(W)+"x"+str(H)),[btn640 ,btn1366, btn1920])
back_btn = Button(W/2-100,600,"Back", menu)

while True:

    for e in event.get():
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            exit()  
        if e.type == MOUSEBUTTONDOWN:
            if mode == "start_screen":
                start_btn.check_click(e.pos)
                settings_btn.check_click(e.pos)
                exit_btn.check_click(e.pos)
            elif mode == "setting":
                res_list.check_click(e.pos)
                btn640.check_click(e.pos)
                btn1366.check_click(e.pos)
                btn1920.check_click(e.pos)
                back_btn.check_click(e.pos)

    
    
    if mode == "start_screen":
        start_menu.update()
        start_btn.update()
        settings_btn.update()
        exit_btn.update()

    elif mode == "setting":
        if res_list.visible == True:
            start_menu.update()
            res_list.update()
            btn640.update()
            btn1366.update()
            btn1920.update()
        else:
            start_menu.update()
            res_list.update()
            btn640.update()
            btn1366.update()
            btn1920.update()
            back_btn.update()

    display.update()
    
