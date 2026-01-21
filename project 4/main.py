import pgzrun
import random

WIDTH = 900
HEIGHT = 900

cookie = Actor("cookieimageremoved")
cookie.pos = (450, 450)

def draw():
    screen.clear()
    cookie.draw()

def update():
    if keyboard.left:
        cookie.x -= 6
        if cookie.x < 0:
            cookie.x= 0

    elif keyboard.right:
        cookie.x += 6
        if cookie.x > WIDTH:
            cookie.x=WIDTH



pgzrun.go()