import pgzrun
import random


WIDTH = 1200
HEIGHT = 600

ship=Actor("galaga.png")

White = (255, 255, 255)
Blue = (0,0,255)

def draw():
    screen.clear()
    screen.fill(Blue)
    ship.draw()

pgzrun.go()