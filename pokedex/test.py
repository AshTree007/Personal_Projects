from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
def hello_world():
    return render_template("frontend.html")

@app.route("/", methods=["POST"])
def random_name():
    return f"{5+2}"