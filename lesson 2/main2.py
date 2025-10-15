import pgzrun
from pgzero.builtins import *
import pgzero.screen
screen: pgzero.screen.Screen



WIDTH = 700
HEIGHT = 700
def draw():
    screen.blit("space", (0,0))

    screen.draw.line((100,100),(200,200), color = "green")
     
pgzrun.go()