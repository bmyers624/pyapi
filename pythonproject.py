#!/usr/bin/python3

from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)

quiz_questions = {
# 'question' : [options]
'Great Pyramid':['Giza','Ancient Greece','Suez','Babylon'],
'Hanging Gardens':['Babylon','Rome','Rio de Janeiro','Giza'],
'Temple of Artemis':['Ephesus','Sparta','Rome','Athens'],
'Tomb of Mausolus':['Halicarnassus','Athens','Pasargadae','Babylon'],
'Colossus':['Rhodes','Sparta','Athens','Ephesus'],
'The Lighthouse':['Alexandria','Athens','Sparta','Olympia'],
'Statue of Zeus':['Olympia','Ephesus','Athens','Sparta']
}

questions = copy.deepcopy(quiz_questions)

def shuffle(q):
    """
    This function shuffles
    the Quiz questions.
    """
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(q.keys())
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i+1
    return selected_keys

@app.route('/')
def quiz():
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('main.html', q = questions_shuffled, o = questions)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
    correct = 0
    for i in questions.keys():
        answered = request.form[i]
        if quiz_questions[i][0] == answered:
            correct = correct+1
    return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == "__main__":
    app.run(debug=True)

