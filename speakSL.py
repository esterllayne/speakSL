from flask import Flask, render_template, request, url_for
import requests
import numpy as np

app=Flask("AppSL")

alphabetD={"a": "https://i.imgur.com/k01IMQh.jpg", "b":"https://i.imgur.com/i64U0Og.jpg","c":"https://i.imgur.com/XY6I3AF.jpg",
"d":"https://i.imgur.com/sLv8lym.jpg","e":"https://i.imgur.com/byfORPL.jpg","f":"https://i.imgur.com/dEGU7Cb.jpg",
"g":"https://i.imgur.com/lW9Usvg.jpg","h":"https://i.imgur.com/T4tbyHM.jpg","i":"https://i.imgur.com/JB6JeJx.jpg",
"j":"https://i.imgur.com/hych0qL.jpg","k":"https://i.imgur.com/eBgmjvw.jpg","l":"https://i.imgur.com/N3OiXqa.jpg",
"m":"https://i.imgur.com/eSNfSQH.jpg","n":"https://i.imgur.com/C6WTAhy.jpg","o":"https://i.imgur.com/7zwLHYZ.jpg",
"p":"https://i.imgur.com/Gm3lOgi.jpg","q":"https://i.imgur.com/1If07uh.jpg","r":"https://i.imgur.com/qt4F7jG.jpg",
"s":"https://i.imgur.com/BSHtJmS.jpg","t":"https://i.imgur.com/amXK8jU.jpg","u":"https://i.imgur.com/RL9roFi.jpg",
"v":"https://i.imgur.com/pGiMgvM.jpg","w":"https://i.imgur.com/mJzLDLp.jpg","x":"https://i.imgur.com/DnIUoVk.jpg",
"y":"https://i.imgur.com/6qEgu6D.jpg","z":"https://i.imgur.com/h6oWvhS.jpg"}

greetingsD={"Hello": "https://i.imgur.com/LaD3P7J.gif","Good Morning":"https://i.imgur.com/sX4ktUG.gif",
"Good Afternoon":"https://i.imgur.com/U5tXIJi.gif","Good Evening":"https://i.imgur.com/KQmsPEY.gif",
"Good Night":"https://i.imgur.com/yA7Bwpj.gif","Thank You!":"https://i.imgur.com/X3z7YBm.gif",
"You're welcome!":"https://i.imgur.com/QV8Aue0.gif",
"How Are You?":"https://i.imgur.com/tSUZYHc.gif",
"I'm fine.":"https://i.imgur.com/YEUrROL.gif",
"What's your name?":"https://i.imgur.com/A7tptou.gif",
"My name is...":"https://i.imgur.com/SozfEPL.gif",
"Nice to meet you!":"https://i.imgur.com/zdOg8TT.gif","Goodbye":"https://i.imgur.com/UygItlu.gif"}

greetingsUncovered={"Hello": "https://media.giphy.com/media/3o7TKNKOfKlIhbD3gY/giphy.gif","Good Morning":"https://media.giphy.com/media/26FLchGgqamznV64E/giphy.gif",
"Good Afternoon":"https://media.giphy.com/media/l4JzaRsX52k8glIFa/giphy.gif","Good Evening":"https://media.giphy.com/media/l4JzdrbDeU2lMMrde/giphy.gif",
"Good Night":"https://media.giphy.com/media/l4Jz5WK4Uddr8KsSc/giphy.gif","Thank You!":"https://media.giphy.com/media/l0MYrlUnFtq25TQR2/giphy.gif",
"You're welcome!":"https://media.giphy.com/media/3o7TKSRNcdPmcNmTGo/giphy.gif",
"How Are You?":"https://media.giphy.com/media/3o7TKDw5NA17fKJVWU/giphy.gif",
"I'm fine.":"https://media.giphy.com/media/l4Jzd71ci3msO66ac/giphy.gif",
"What's your name?":"https://media.giphy.com/media/3o7TKDJBonanzESryE/giphy.gif",
"My name is...":"https://media.giphy.com/media/3o7TKzkaMOHallCppe/giphy.gif",
"Nice to meet you!":"https://media.giphy.com/media/1oHlX1mrGBF5xu1ks1/giphy.gif","Goodbye":"https://media.giphy.com/media/3o7TKzb3i29i86BPJm/giphy.gif"}





def evaluate_score(ansUsr,ansCorrect):
    score=0
    for i in range(len(ansUsr)):
       if ansUsr[i].lower()==ansCorrect[i].lower():
           score=score+1
       else:
            score=score
    
    percentSc=round(100*score/len(ansUsr))
    scoreL=[score,percentSc]
    return  scoreL

def pick(theDict): # randomly selects 6 items from a dictionary (in this case greetingsD) and returns a dictionary of the 6  chosen items
    pickedLetters = np.random.choice(a=list(theDict),size=6,replace=False)  
    return dict( (k, theDict[k]) for k in pickedLetters if k in theDict)


@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/greetings")
def get_greetings():
    return render_template("greetings.html")


@app.route("/small")
def get_small():
    return render_template("small.html")


@app.route("/alphabet")
def get_alphabet():
    return render_template("alphabet.html")

@app.route("/quiz")
def get_quiz():
    return render_template("quiz.html")

@app.route("/quizG")
def get_quizG():
    greetingLabels=['Q1','Q2','Q3','Q4','Q5','Q6']
    greetingsIDs=['id1','id2','id3','id4','id5','id6']
    PickedGreetings=pick(greetingsD)
    return (render_template("quizG.html",PickedGreetings=PickedGreetings,qLabels=greetingLabels,gIDs=greetingsIDs,answerOptions=greetingsD))


@app.route("/quizA")
def get_quizA():
    questionLabels=['Q1','Q2','Q3','Q4','Q5','Q6']
    questionIDs=['id1','id2','id3','id4','id5','id6']
    PickedLettersDict=pick(alphabetD)
    return (render_template("quizA.html",PickedLettersDict=PickedLettersDict,qLabels=questionLabels,qIDs=questionIDs))


@app.route("/resultsQuiz", methods=["POST"])
def returnResults():
    form_data=request.form
    correctLetters=[form_data["Q1"],form_data["Q2"],form_data["Q3"],form_data["Q4"],form_data["Q5"],form_data["Q6"]]
    userAnswers=[form_data["id1"], form_data["id2"], form_data["id3"], form_data["id4"],form_data["id5"],form_data["id6"] ]
    your_score=evaluate_score(userAnswers,correctLetters)[0]
    your_scorePerc=evaluate_score(userAnswers,correctLetters)[1]
    return render_template("resultsQuiz.html",your_score=your_score,your_scorePerc=your_scorePerc)

# @app.route("/resultsQuizG", methods=["POST"])
# def returnResultsG():
#     print(request.form)
#     return render_template("temporary.html")

@app.route("/resultsQuizG", methods=["POST"])
def returnResultsG():
    form_data=request.form
    print('---request form:----')
    print(request.form)
    correctAnswers= [form_data["Q1"],form_data["Q2"],form_data["Q3"],form_data["Q4"],form_data["Q5"],form_data["Q6"]]
    userAnswers=[form_data["id1"], form_data["id2"], form_data["id3"], form_data["id4"],form_data["id5"],form_data["id6"] ]
    your_score=evaluate_score(userAnswers,correctAnswers)[0]
    your_scorePerc=evaluate_score(userAnswers,correctAnswers)[1]
    print('---userAnswers:---')
    print(userAnswers)
    print(' ----correct answers: ---')
    print(correctAnswers)
    print(' ----len user answer: ---')
    print(len(userAnswers))
    print(' ----len correct answers: ---')
    print(len(correctAnswers))
    return render_template("resultsQuizG.html",your_score=your_score,your_scorePerc=your_scorePerc)


if "AppSL" == '__main__':
    app.run()

# To run locally comment out the if above and uncomment below. then just run python speakSL
# app.run(debug=True)