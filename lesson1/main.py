import pgzrun
from pgzero.builtins import *
import pgzero.screen
screen: pgzero.screen.Screen



WIDTH = 700
HEIGHT = 700

Maat = Actor("alein2.0")

def draw():
    screen.blit("space", (0,0))
    Maat.draw()

def on_mouse_down(pos):
    if Maat.collidepoint(pos):
        print("AWESOME")




pgzrun.go()