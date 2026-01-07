import pgzrun


WIDTH = 1200
HEIGHT = 600


WHITE = (255, 255, 255)
BLUE = (0,0,255)
speed = 5

ship=Actor("galaga.png")

ship.pos = (WIDTH//2,HEIGHT-60)

def update():
    if keyboard.left:
        ship.x-=speed
        if ship.x<=0:
            ship.x=0


    elif keyboard.right:
        ship.x+=speed
        if ship.x>=WIDTH:
            ship.x=WIDTH

def draw():
    screen.clear()
    screen.fill(BLUE)
    ship.draw()



pgzrun.go()