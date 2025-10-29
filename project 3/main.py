import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen: pgzero.screen.Screen


WIDTH = 700
HEIGHT = 600

items=["bagimg","batteryimg","bottleimg","chipsimg","paperimg",]
main_item = "purple-star"
selected_items = []

def setup():
    main_actor= Actor(main_item)
    selected_items.append(main_actor)

def draw():
    screen.blit("bground", (0,0))
    for items in selected_items:
        items.draw()

setup()
pgzrun.go()
