import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen:pgzero.screen.Screen

WIDTH = 700
HEIGHT = 600

level = 2
total_items = level*2

items=["bagimg","batteryimg","bottleimg","chipsimg","paperimg",]
main_item = "purple-star"
selected_items = []


def setup():
    main_actor= Actor(main_item)
    selected_items.append(main_actor)
    for i in range(total_items-1):
        rand_item = random.choice(items)
        random_actor = Actor(rand_item)
        selected_items.append(random_actor)
    random.shuffle(selected_items)
    gap = WIDTH/(total_items+1)
    for i in range(total_items):
        curr_item = selected_items[i]
        curr_item.pos = (gap* (i+1)),40
def draw():
    screen.blit("bground", (0,0))
    for items in selected_items:
        items.draw()

setup()
pgzrun.go()
