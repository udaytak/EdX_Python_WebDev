from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def forms():
    return render_template("forms.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please Submit the forms instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)