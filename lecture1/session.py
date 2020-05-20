from flask import Flask, render_template, request, session
from flask_session import session

app.Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/" , method = ["GET", "POST"])
def session():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    
    return render_template("session.html", notes= notes)