# import pgzrun
# from pgzero.builtins import*
# import pgzero.screen
# import random
# screen:pgzero.screen.Screen

# WIDTH = 700
# HEIGHT = 700

# box = Rect((30, 200), (550, 120))

# def draw():
#     screen.draw.filled_rect(box, "blue")

     






# pgzrun.
import pgzrun
from pgzero.builtins import Rect
import pgzero.screen
screen:pgzero.screen.Screen
import random
WIDTH = 900
HEIGHT = 900

question_bank = []

with open("project 4\questions.txt", "r") as file:
    data = file.readlines()

    for line in data:
        question = line.split(",")
        print(question)
        cookie = {
            "question":question[0],
            "options":question[1:5],
            "answer":question[5]
        }
        question_bank.append(cookie)



coca = random.choice(question_bank)


box = Rect((10, 70), (550, 120))
box2 = Rect((10,270), (250,120))
box3 = Rect((10,470), (250,120))
box4 = Rect((300,470), (250,120))
box5 = Rect((300,270), (250,120))
box6 = Rect((600,70), (150,120))
box7 = Rect((600,270), (150,320))
def draw():
    screen.clear()
    screen.draw.filled_rect(box, "blue")
    screen.draw.filled_rect(box2, "orange")
    screen.draw.filled_rect(box3, "orange")
    screen.draw.filled_rect(box4, "orange")
    screen.draw.filled_rect(box5, "orange")
    screen.draw.filled_rect(box6, "orange")
    screen.draw.filled_rect(box7, "orange")
    screen.draw.text(coca["question"], color = "white", pos = (120,150), fontsize = 25 )


def update():
    pass

pgzrun.go()
