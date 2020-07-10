#!/usr/bin/python3

from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)

quiz_questions = { # questions dictionary
# 'question' : [options]
'Great Pyramid':['Giza','Ancient Greece','Suez','Babylon'],
'Hanging Gardens':['Babylon','Rome','Rio de Janeiro','Giza'],
'Temple of Artemis':['Ephesus','Sparta','Rome','Athens'],
'Tomb of Mausolus':['Halicarnassus','Athens','Pasargadae','Babylon'],
'Colossus':['Rhodes','Sparta','Athens','Ephesus'],
'The Lighthouse':['Alexandria','Athens','Sparta','Olympia'],
'Statue of Zeus':['Olympia','Ephesus','Athens','Sparta']
}

questions = copy.deepcopy(quiz_questions) # made deep copy of the original questions dictionary so that any changes made to the copy won't affect the original, i.e. 'shuffle'

#def shuffle(q): 
#    # created this function to shuffle the keys from the questions dictionary.
#    # could possibly fix problem by just calling 'random.shuffle(questions.keys())' instead of this
#    """
#    This function shuffles
#    the Quiz questions.
#    """
#    selected_keys = []
#    i = 0
#    while i < len(q):
#        current_selection = random.choice(q.keys())
#        if current_selection not in selected_keys:
#            selected_keys.append(current_selection)
#            i = i+1
#    return selected_keys

@app.route('/')
def quiz():
#    questions_shuffled = shuffle(questions) # the questions are being shuffled and the result is a list that is stored in variable 'questions_shuffled'
    questions_shuffled = random.choice(list(questions.items())) 
    # the shuffle problem was fixed by replacing it with this command, in python3 d.keys() returns a dict_keys object
    #  which is more like a set than a list, so it couldnt be indexed. Therefore the solution to the problem was to pass list(d.items()) to random
    for i in questions.keys(): # for loop to loop through keys of questions dictionary
        random.shuffle(questions[i]) # all values in list of questions are shuffled
    return render_template('main.html', q = questions_shuffled, o = questions) # the values are returned to template/main.html

@app.route('/quiz', methods=['POST'])
def quiz_answers():
    correct = 0
    for i in questions.keys(): # using for loop to loop through keys of questions dictionary
        answered = request.form[i] # access value selected by user, using request
        if quiz_questions[i][0] == answered: # correct answer is first element in list of dictionary of questions (the original, not the copy)
            correct = correct+1
    return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == "__main__":
    app.run(debug=True)

