import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen: pgzero.screen.Screen



WIDTH = 700
HEIGHT = 550
score = 0
message = ""
Maat = Actor('alein2.0')
def draw():
    screen.blit("space", (0,0))
    Maat.draw()
    screen.draw.text(message,color="orange",center = (400,70))
    screen.draw.text(f"score:{score}",color="pink",center = (100,70))
def on_mouse_down(pos):
    global message,score
    if Maat.collidepoint(pos):
        score+=1
        message = ("AWESOME")
        Maat.pos = (random.randint(20,480),(random.randint(20,480)))
    else:
        message = "take a shot if you dare"

def update():
    pass
pgzrun.go()