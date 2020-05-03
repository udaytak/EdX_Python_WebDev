from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World !"

@app.route("/david")
def david():
    return "Hello, David !"

if __name__ == "__main__":
    app.run(debug=True)