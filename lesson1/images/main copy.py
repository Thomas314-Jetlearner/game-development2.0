import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen: pgzero.screen.Screen



WIDTH = 700
HEIGHT = 550
   
def draw():
    screen.blit("brick", (0,0))
    screen.draw.line((100,100),(100,150),color = "white")

pgzrun.go()