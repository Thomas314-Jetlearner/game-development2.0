import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen: pgzero.screen.Screen


WIDTH = 700
HEIGHT = 550

cookie = Actor('cookiess')
micro = Actor('microphone') 

def draw():
    screen.blit("space", (0,0))
    cookie.draw()
    micro.draw()


def update():
    micro.y+=1
    cookie.x+=2
pgzrun.go()