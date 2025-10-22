import pgzrun
from pgzero.builtins import *
import pgzero.screen
import random
screen: pgzero.screen.Screen


WIDTH = 600
HEIGHT =500
sats = []
curr_ind = 1
start_cords = []
end_cords = []
lis = []
gameover = False
for i in range(8):
    sat = Actor("satellite")
    sat.pos = random.randint(50,550),random.randint(50,450)
    sats.append(sat)


def draw():
    
    screen.blit("space" , (0,0))
    if gameover:
        screen.draw.text("GAMEOVER!!!??",color = "blue", center = (200,200),fontsize = 70)
    else:
        for i in range(8):
            sats[i].draw()
            screen.draw.text(str(i+1),center= (sats[i].x+20,sats[i].y))
        for i in range(len(end_cords)):
            screen.draw.line(start_cords[i],end_cords[i] , color = "orange")
    # else:
    #     start_cords.clear()
    #     end_cords.clear()
       
    


def on_mouse_down(pos):
    global curr_ind,gameover
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
   
    else:
        gameover = True
     

pgzrun.go()