from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("first.html")

@app.route("/more")
def more():
    return render_template("more.html")