import pgzrun


WIDTH = 1200
HEIGHT = 600


WHITE = (255, 255, 255)
BLUE = (0,0,255)
speed = 5

ship=Actor("galaga.png")

ship.pos = (WIDTH//2,HEIGHT-60)

bullets = []
enemies = []


for x in range(8):
    enemies.append(Actor("bug"))
    enemies[-1].x = 100+90*x
    enemies[-1].y = 80

score = 0
direction = 1

def display_score():
    screen.draw.text(str(score),(50,30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50


def update():
    global score
    global direction
    move_down = False

    if keyboard.left:
        ship.x-=speed
        if ship.x<=0:
            ship.x=0


    elif keyboard.right:
        ship.x+=speed
        if ship.x>=WIDTH:
            ship.x=WIDTH

    if keyboard.space:
        print("pressing space")
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y


    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y-=10
    
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        move_down = True
        direction=direction*-1

    for enemy in enemies:
        enemy.x+=5*direction
        if move_down == True:
            enemy.y+=50


        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.s1.play()
                score+=100
                bullets.remove(bullet)
                enemies.remove(enemy)






def draw():
    screen.clear()
    screen.fill(BLUE)
    

    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

    ship.draw()
    display_score() 

pgzrun.go()