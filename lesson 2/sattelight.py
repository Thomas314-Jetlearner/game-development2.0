import pgzrun
import random

WIDTH = 600
HEIGHT =700
sats = []
curr_ind = 1
start_cords = []
end_cords = []
for i in range(8):
    sat = Actor("satellite")
    sat.pos = random.randint(50,550),random.randint(50,650)
    sats.append(sat)


def draw():
    screen.blit("space" , (0,0))
    for i in range(8):
        sats[i].draw()
        screen.draw.text(str(i+1),center= (sats[i].x+20,sats[i].y))
    for i in range(len(end_cords)):
        screen.draw.line(start_cords[i],end_cords[i] , color = "orange")
def on_mouse_down(pos):
    global curr_ind
    if curr_ind<8:
        curr_sat = sats[curr_ind]
        prev_sat = sats[curr_ind-1]
        if curr_sat.collidepoint(pos):
            start_cords.append(prev_sat.pos)
            end_cords.append(curr_sat.pos)
            curr_ind+=1
        else:
            start_cords.clear()
            end_cords.clear()
            curr_ind = 1

     

pgzrun.go()