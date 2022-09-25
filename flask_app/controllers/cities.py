from flask_app import app
from flask import render_template, request, redirect, session

@app.route("/")
def new_user_form():
    return render_template("index.html")



@app.route("/add_data" , methods=["POST"])
def add_user():
    session["name"] = request.form["name"]
    session["dojo"] = request.form["dojo"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")

@app.route("/results")
def show_results():
    return render_template("results.html")