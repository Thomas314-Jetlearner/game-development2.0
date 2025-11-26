import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen:pgzero.screen.Screen

WIDTH = 700
HEIGHT = 600
picture = ["spock", "darlek"]
# spock = Actor("Mr.spock")
darlek = Actor("download")
# duck = Actor("penguin")

mess = ""

def draw():
    screen.blit("bground", (0,0))
    darlek.draw()
    # duck.draw()
    if mess:
        screen.draw.text(mess,color="orange",center = (80,80))

def on_mouse_down(pos):
    global mess
    if darlek.collidepoint(pos):
        mess = "EXTERMINATE"

    elif duck.collidepoint(pos):
        mess = "DUCK DUCK DUCK!!!"

    
pgzrun.go()


