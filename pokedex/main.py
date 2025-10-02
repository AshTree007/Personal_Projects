import requests as req
from flask import Flask, render_template, request, redirect

#sets app
app = Flask(__name__)
#base url for the pokeapi
url = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        pokemon_name = request.form.get("poke_name").lower()
        return redirect(f"/{pokemon_name}")
    return render_template("frontend.html")

@app.route("/<pokemon_name>", methods=["POST", "GET"])
def get_info(pokemon_name):
    if request.method == "POST":
        return redirect("/")
    print(url+pokemon_name)
    r = req.get(url+pokemon_name) #completes url and makes get request
    if r.status_code == 200:
        r = r.json() #turns json response into a dictionary
        # gets variables
        img = r["sprites"]["front_default"]
        name = r["name"].capitalize()
        id = r["id"]
        height = r["height"]
        weight = r["weight"]
        return render_template("response.html", img = img, name = name, id = id, height = height, weight=weight)
    else:
        return redirect("/")