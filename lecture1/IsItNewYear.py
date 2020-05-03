import datetime

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.day == 1 and now.month == 1
    return render_template("newYear.html",new_year=new_year)
