from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def first1():
    return render_template("first1.html")

@app.route("/second1")
def second1():
    return render_template("second1.html")