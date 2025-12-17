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
        print(ques)
        ginger = {"questions":[0], "option":[1:5], "answer":[5]}
        questions.append(ginger)

powder = random.choice(questions)












