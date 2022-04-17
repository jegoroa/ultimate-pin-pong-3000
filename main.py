from pygame import *

lightgreen = (0,255,100)

win = display.set_mode((1000,500))

while True:

    for e in event.get():
        if e.type == QUIT:
            exit()

    win.fill(lightgreen)
    display.update()