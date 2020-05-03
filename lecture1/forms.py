from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def forms():
    return render_template("forms.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)