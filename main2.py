import pgzrun
from pgzero.builtins import *
import pgzero.screen
screen: pgzero.screen.Screen



WIDTH = 700
HEIGHT = 700

alien = Actor('alein2.0')

def draw():
    screen.clear()
    alien.draw()
    
    
    
    
    
    
    
    pgzrun.go()