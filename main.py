from pygame import *
from pong import *
from random import randint

import json

with open("database.json","r",encoding="utf-8") as file:
    database = json.load(file)

init()

hit_sound = mixer.Sound('hit_sound.wav')
music = mixer.Sound('music.wav')

vfaces = ["up", "dawn"]
hfaces = ["right","left"]

first_player = 0
second_player = 0

new_skin = 0
in_game = False

bg = transform.scale(bg , (W, H))

mode = "start_screen"
#пмапсаммамммммс
def start():
    global mode, in_game
    mode = "game"
    in_game = True

def setting():
    global mode
    mode = "setting"

def resume():
    global mode
    mode = "game"

def menu():
    global mode, first_player, second_player, in_game
    if in_game == True:
        mode = "menu"
    else:
        mode = "start_screen"

def shop_menu():
    global mode, first_player, second_player, in_game
    in_game = False
    mode = "start_screen"
    first_player = 0
    second_player = 0


def shop():
    global mode
    mode = "shop"

def choose_skin():
    global new_skin
    ball.change_skin(database["skin_list"][new_skin])
    new_skin = 0

def next_skin():
    global new_skin
    new_skin += 1
    if new_skin >= len(database["skin_list"]):
        new_skin = 0
    skin_pic.image = transform.scale(image.load(database["skin_list"][new_skin]), (200,200))

def back_skin():
    global new_skin
    new_skin -= 1
    if new_skin < 0:
        new_skin = len(database["skin_list"])-1
    skin_pic.image = transform.scale(image.load(database["skin_list"][new_skin]), (200,200))

def sound_audio():
    if hit_sound.get_volume() == 1:
        hit_sound.set_volume(0)
    else:
        hit_sound.set_volume(1)

def music_audio():
    if music.get_volume() == 0.09375:
        music.set_volume(0)
    else:
        music.set_volume(0.1)

lightgreen = (0,255,100)

#class

class PlatForm():
    def __init__(self,x,y,width,height,speed,pic_name):
        self.height = height
        self.pic = image.load(pic_name)
        self.pic = transform.scale(self.pic, (width,height))
        self.rect = Rect(x,y,width,height)
        self.speed = speed

    def update(self):
        if self.ymove == 'down':
            self.rect.y += self.speed
            if self.rect.y > H-self.height:
                self.rect.y = H-self.height
        else:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0

        #столкиваюсь ли я с мячом???
        if self.rect.colliderect(ball.rect):
            hit_sound.play()
            #если да
            #то меняю у него направление движения по горизонтали
            if ball.hface == "right": ball.hface = "left"
            else: ball.hface = "right"
        
        #бонус - добавить +1 балл игроку за отбив мяча

        self.reset()

    def reset(self):
        win.blit(self.pic,( self.rect.x,self.rect.y))

class Mychik():
    def __init__(self,x,y,w,h,speed,filename,vface,hface):
        self.w = w
        self.h = h
        self.height = h
        self.speed = speed
        self.filename = filename
        self.rect = Rect(x,y,w,h)
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (w,h))
        self.rect.x = x
        self.rect.y = y
        self.vface = vface
        self.hface = hface

    def change_skin(self,new_filename):
        self.image = image.load(new_filename)
        self.image = transform.scale(self.image, (self.w,self.h))

    def reset(self):
        win.blit( self.image , (self.rect.x, self.rect.y) )

    def update(self):
        global mode, loose_label

        if self.hface == "right":
            self.rect.x += self.speed
            
            if self.rect.x > W:
                #проигрывает игрок 2
                self.rect.x = W/2
                self.rect.y = H/2
                global second_player
                self.vface, self.hface = vfaces[randint(0,1)],hfaces[randint(0,1)]
                second_player +=1
                if second_player == 5:
                    mode = "end_game"
                
        if self.hface == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                #проигрывает игрок 1
                self.rect.x = W/2
                self.rect.y = H/2
                global first_player
                self.vface, self.hface = vfaces[randint(0,1)],hfaces[randint(0,1)]
                first_player +=1
                if first_player == 5:
                    mode = "end_game"

        if self.vface == "up":
            self.rect.y -= self.speed
            if self.rect.y < 0:
                hit_sound.play()
                self.vface = "dawn"

        if self.vface == "dawn":
            self.rect.y += self.speed
            if self.rect.y > H-self.height:
                hit_sound.play()
                self.vface = "up"

        self.reset()

#start_screen
start_menu = Menu(W/2-250,H/2 - 100, "layer.png")
start_btn = Button(W/2-100,H/2,"UI\\buttons\\start_btn.png", start)#Algerian 200pt
settings_btn = Button(W/2-100,H/2 + 100 , "UI\\buttons\\settings_btn.png", setting)

shop_btn = Button(W/2-100,H/2 + 200 , "UI\\buttons\\shop_btn.png", shop)

exit_btn = Button(W/2-100,H/2 + 300,"UI\\buttons\\exit_btn.png", exit)

#setting

back_btn = Button(100,100,"UI\\buttons\\back_btn.png", menu)

    #grafical
btn2560 = Button(300,200,"UI\\buttons\\res\\2560x1440_btn.png",set_2560)#Algerian 150pt
btn1920 = Button(300,300,"UI\\buttons\\res\\1920x1080_btn.png",set_1920)
btn1366 = Button(300,400,"UI\\buttons\\res\\1366x768_btn.png",set_1366)
btn640 = Button(300,500,"UI\\buttons\\res\\640x480_btn.png", set_640)
res_list = ListButton(300,100,"UI\\buttons\\resize_btn.png",[btn640, btn1366, btn1920, btn2560])

    #music
music_controller = Button(500,200 ,"UI\\buttons\\music_btn.png", music_audio)
sound_controller = Button(500,300 ,"UI\\buttons\\sound_btn.png", sound_audio)
audio_list = ListButton(500,100 ,"UI\\buttons\\audio_btn.png",[music_controller, sound_controller])


#game
platform = PlatForm(x=100,y=H/2,width=int(H/20),height=int(W/11),speed=10,pic_name="platform.png")
platform.ymove = "-"

platform1 = PlatForm(x=(W-100),y=H/2,width=int(H/20),height=int(W/11),speed=10,pic_name="platform.png")
platform1.ymove = "-"


ball = Mychik(W/2,H/2,int(H/20),int(H/20),10,'skins\\beach-ball-icon.png',vfaces[randint(0,1)],hfaces[randint(0,1)])

#menu
resume_btn = Button(W/2-100,H/2,"UI\\buttons\\resume_btn.png", resume)

#shop

back_skin_btn = Button(W/2-200,H/2 + 200,"UI\\buttons\\button.png", back_skin, w  = 100)
choose_skin = Button(W/2-100,H/2 + 200,"UI\\buttons\\choose_btn.png", choose_skin)
next_skin_btn = Button(W/2 + 100,H/2 + 200,"UI\\buttons\\button.png", next_skin, w = 100)
skin_pic = Picture(W/2-100,H/2, 200, 200, database["skin_list"][0])
shop_back_btn = Button(W/2-100,H/2 + 300,"UI\\buttons\\back_btn.png", shop_menu)

#end
right_lose = Menu(W/2-250,H/2 - 100, "right_lose.png")
left_lose = Menu(W/2-250,H/2 - 100, "left_lose.png")

w = W
h = H

timer = time.Clock()
    
music.play(-1)
music.set_volume(0.1)
while True:    
    for e in event.get():
        if (e.type == KEYDOWN and e.key == K_ESCAPE) or e.type == QUIT:
            if mode == "menu":
                mode = "game"
                in_game == True
            elif in_game == True:
                mode = "menu" 
        
        if e.type == MOUSEBUTTONDOWN:
            if mode == "start_screen":
                start_btn.check_click(e.pos)
                settings_btn.check_click(e.pos)
                shop_btn.check_click(e.pos)
                exit_btn.check_click(e.pos)
            elif mode == "setting":
                res_list.check_click(e.pos)
                audio_list.check_click(e.pos)
                back_btn.check_click(e.pos)
                if audio_list.visible == True:
                    music_controller.check_click(e.pos) 
                    sound_controller.check_click(e.pos)
                if res_list.visible == True:
                    btn640.check_click(e.pos)
                    btn1366.check_click(e.pos)
                    btn1920.check_click(e.pos)
                    btn2560.check_click(e.pos)
            elif mode == "shop":
                back_skin_btn.check_click(e.pos)
                choose_skin.check_click(e.pos)
                next_skin_btn.check_click(e.pos)
                shop_back_btn.check_click(e.pos)

            elif mode == "menu":
                resume_btn.check_click(e.pos)
                settings_btn.check_click(e.pos)
                shop_back_btn.check_click(e.pos)

            elif mode == "end":
                back_btn.check_click(e.pos)                
        
        if e.type == KEYDOWN:
            if e.key == K_w:
                platform.ymove = "up"

            if e.key == K_s:
                platform.ymove = "down"

            if e.key == K_UP:
                platform1.ymove = "up"

            if e.key == K_DOWN:
                platform1.ymove = "down"

    if mode == "start_screen":
        win.blit(bg,(0,0))
        start_menu.update()
        start_btn.update()
        shop_btn.update()
        settings_btn.update()
        exit_btn.update()

    elif mode == "setting":
        win.blit(bg,(0,0))
        res_list.update()
        btn640.update()
        btn1366.update()
        btn1920.update()
        btn2560.update()
        audio_list.update()
        sound_controller.update()
        music_controller.update()
        back_btn.update()

    elif mode == "shop":
        win.blit(bg,(0,0))
        start_menu.update()
        back_skin_btn.update()
        choose_skin.update()
        next_skin_btn.update()
        skin_pic.update()
        shop_back_btn.update()
    
    elif mode == "game":
        score1 = menu_font.render(str(first_player), True, (0,0,0))
        score2 = menu_font.render(str(second_player), True, (0,0,0))
        win.blit(bg,(0,0))
        win.blit(score1,(100*1*(W/1080),42))
        win.blit(score2,(W-100*1*(W/1080),42))
        ball.update()
        platform.update()
        platform1.update()

    elif mode == "menu":
        win.blit(bg,(0,0))
        win.blit(score1,(100*1*(W/1080),42))
        win.blit(score2,(W-100*1*(W/1080),42))
        start_menu.update()
        resume_btn.update()
        settings_btn.update()
        shop_back_btn.update()     

    elif mode == "end_game":
        win.blit(bg,(0,0))
        if first_player == 5:
            left_lose.update()
            shop_back_btn.update()

        if second_player == 5:
            right_lose.update()
            shop_back_btn.update()


    timer.tick(60)
    display.update()

