import random
import json


def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]

    return questions

questions = load_questions()
print(questions)

#clt+tab+y