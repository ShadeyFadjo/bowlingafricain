from flask import Flask
from markupsafe import escape
from flask import render_template
from urllib.parse import unquote

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Accueil, Kal!</p>"

@app.route('/accueil/<pays>')
def kal(pays=None):
    nompays=escape(pays.replace('_',' '))
    return render_template('accueil.html',nompays=nompays)

