#Jeopardy

import json 


class category:
    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)

class question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
with open('jeopardy.json') as f:
    data = json.load(f)

