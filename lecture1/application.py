from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World !"

@app.route("/david")
def david():
    return "Hello, David !"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)