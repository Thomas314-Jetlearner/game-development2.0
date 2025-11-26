import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen:pgzero.screen.Screen

WIDTH = 700
HEIGHT = 600

level = 1
DURATION = 10
score = 0
# screen.draw.text(f"score:{score}",color="blue",center = (300,300))

items=["bagimg","batteryimg","bottleimg","chipsimg","paperimg",]
main_item = "purple-star"
selected_items = []
selected_items_string = []
animations = []
def setup():
    total_items = level*2
    selected_items.clear()
    selected_items_string.clear()
    selected_items_string.append(main_item)
    for i in range(total_items-1):
        rand_item = random.choice(items)
        selected_items_string.append(rand_item)
    random.shuffle(selected_items_string)
    gap = WIDTH/(total_items+1)
    for i in range(total_items):
        curr_item_string = selected_items_string[i]
        curr_item = Actor(curr_item_string)
        curr_item.pos = (gap* (i+1)),40
        selected_items.append(curr_item)
    animate_actors()

def animate_actors():
    for items in selected_items:
        animates = animate(items,duration=DURATION,y = HEIGHT-20)
        animations.append(animates)
def stop_animations():
    for item in animations:
        animations.stop()
        animations = []
    
if level==3:
    stop_animations()
    screen.clear()
    screen.draw.text("GAMEOVER", color = "blue",center = (300,300))
    
    






# def update():
#     for i in range(10):
#         if curr_item.y>HEIGHT-20:
#             screen.clear()
#             screen.draw.text("GAMEOVER!!!", color = "white", center =(300,300))
#             break
    

def draw():
    screen.blit("bground", (0,0))
    for items in selected_items:
        items.draw()

def on_mouse_down(pos):
    global level, DURATION
    for i in range(len(selected_items)):
        curr_item = selected_items[i]
        if curr_item.collidepoint(pos):
            if selected_items_string[i] == main_item:
                level+=1
                DURATION-=1
                # score+=1
                setup()

setup()
pgzrun.go()
