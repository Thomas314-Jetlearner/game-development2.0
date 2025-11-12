import pgzrun
import random



WIDTH = 500
HEIGHT = 600

def setup():
    for i in range(10):
        cookie = Actor("purple-star")
        cookie.pos = (random.randint(20,480),random.randint(20,580))
        cookies.append(cookie)
cookies = []
setup() 

def draw():
    screen.blit("bg" , (0,0))
    for cookie in cookies:
        cookie.draw()
    
        
    
   



pgzrun.go()
