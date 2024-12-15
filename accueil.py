from flask import Flask
from markupsafe import escape
from flask import render_template, request,redirect, url_for
from urllib.parse import unquote
from game import Game

app = Flask(__name__)
game=Game()

@app.route("/")
def index():
    return render_template('accueil.html',game=game)

@app.route("/submit", methods=["POST"])
def submit():
    pins_knocked=request.form.get("pins_knocked")
    game.calculate_score(int(pins_knocked))
    return redirect(url_for("index"))

@app.route("/init", methods=["POST"])
def init():
    game.current_score=0
    game.frame=1
    game.throw=1
    game.frame_score=0
    game.rest_pins=15 
    game.bonus=0 
    return redirect(url_for("index"))

@app.route("/bonus", methods=["POST"])
def bonus():
    pins_knock=request.form.get("pins_knock")
    game.frame_score+=int(pins_knock)
    game.end_frame()
    return redirect(url_for("index"))