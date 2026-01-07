import pgzrun
from pgzero.builtins import Rect
import pgzero.screen
import random
screen:pgzero.screen.Screen

WIDTH = 900
HEIGHT = 900

box = Rect((100,100), (50,50))
box2 = Rect((200,200), (50,50))
box3 = Rect((300,300), (50,50))
box4 = Rect((400,400), (50,50))

colours = ["red", "green", "blue", "black"]
mylist = [box, box2, box3, box4]

def draw():
    screen.draw.filled_rect(box, "blue")
    screen.draw.textbox("button1",box, color = random.choice(colours))

    screen.draw.filled_rect(box2, "blue")
    screen.draw.textbox("button2",box2, color = random.choice(colours))

    screen.draw.filled_rect(box3, "blue")
    screen.draw.textbox("button3",box3, color = random.choice(colours))

    screen.draw.filled_rect(box4, "blue")
    screen.draw.textbox("button4",box4, color = random.choice(colours))

def on_mouse_down(pos):
    for rect in mylist:
        if rect.collidepoint(pos):
            print("Box clicked")


        






pgzrun.go()








