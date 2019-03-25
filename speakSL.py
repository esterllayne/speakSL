from flask import Flask, render_template, request, url_for
import requests

app=Flask("AppSL")

corrects=['y','l','o','d','i','b']

def evaluate_score(ansUsr,ansCorrect):
    score=0
    for i in range(len(ansUsr)):
       if ansUsr[i].lower()==ansCorrect[i]:
           score=score+1
    percentSc=round(100*score/len(corrects))
    scoreL=[score,percentSc]
    return  scoreL

@app.route("/")
def get_quiz():
    return render_template("quiz.html")

@app.route("/QuizResults", methods=["POST"])
def returnResults():
    form_data=request.form

    userAnswers=[form_data["Q1"],form_data["Q2"],form_data["Q3"],form_data["Q4"],form_data["Q5"],form_data["Q6"]]

    your_score=evaluate_score(userAnswers,corrects)[0]
    your_scorePerc=evaluate_score(userAnswers,corrects)[1]
    return render_template("ResultsQ.html",your_score=your_score,your_scorePerc=your_scorePerc)


if "AppSL" == '__main__':
    app.run()