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

def evaluate_score(ansUsr,ansCorrect):
    score=0
    for i in range(len(ansUsr)):
       if ansUsr[i].lower()==ansCorrect[i]:
           score=score+1
       else:
            score=score
    
    percentSc=round(100*score/len(ansUsr))
    scoreL=[score,percentSc]
    return  scoreL

def pick(theDict): 
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

@app.route("/alphabet")
def get_quiz():
    return render_template("quiz.html")

@app.route("/quizG")
def get_quizG():
    questionLabels=['Q1','Q2','Q3','Q4','Q5','Q6']
    PickedLettersDict=pick(alphabetD)
    return (render_template("quizG.html",PickedLettersDict=PickedLettersDict,qLabels=questionLabels))


@app.route("/quizA")
def get_quizA():
    questionLabels=['Q1','Q2','Q3','Q4','Q5','Q6']
    PickedLettersDict=pick(alphabetD)
    return (render_template("quizA.html",PickedLettersDict=PickedLettersDict,qLabels=questionLabels))


@app.route("/resultsQuiz", methods=["POST"])
def returnResults():
    form_data=request.form
    correctLetters=[form_data["Q1"],form_data["Q2"],form_data["Q3"],form_data["Q4"],form_data["Q5"],form_data["Q6"]]
    print(correctLetters)
    userAnswers=[form_data[correctLetters[0]], form_data[correctLetters[1]], form_data[correctLetters[2]], form_data[correctLetters[3]],
    form_data[correctLetters[4]], form_data[correctLetters[5]] ]
    your_score=evaluate_score(userAnswers,correctLetters)[0]
    your_scorePerc=evaluate_score(userAnswers,correctLetters)[1]
    return render_template("resultsQuiz.html",your_score=your_score,your_scorePerc=your_scorePerc)



if "AppSL" == '__main__':
    app.run()