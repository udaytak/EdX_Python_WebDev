from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def loops():
    names = ["Alice", "Bob", "Charlie","David"]
    return render_template("loops.html", names=names)