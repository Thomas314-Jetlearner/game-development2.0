import pgzrun
import random
import pgzero.screen

WIDTH = 900
HEIGHT =900

questions = []

with open("project 4/questions copy.txt", "r" ) as file:
    data = file.readlines()

    for l in data:
        ques = l.split("|")
        ginger = {"questions":ques[0], "option":ques[1:5], "answer":ques[5]}
        questions.append(ginger)

powder = random.choice(questions)
print(powder)












