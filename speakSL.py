from flask import Flask, render_template, request
import requests


app=Flask("AppSL")


@app.route("/quiz")
def get_quiz():
    return render_template("quiz.html")



@app.route("/signup", methods=["POST"])
def returnhome():
    form_data=request.form
    v_email=form_data["email"]
    send_simple_message(sendTo_mail=form_data["email"],sendTo_name=form_data["name"])
    return render_template("programming.html",v_email=v_email)



app.run(debug=True)