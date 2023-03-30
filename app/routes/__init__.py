from flask import render_template, request
from app import app
from app.models import Pokemons

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/pokemons", methods=['GET'])
def pokemons():
    nome = request.args.get('nome')
    if nome:
        pokemon = Pokemons.query.filter_by(nome=nome).first()
        return render_template("pokemons.html", pokemon=pokemon)
    else:
        pokemons = Pokemons.query.all()
        return render_template("pokemons.html", pokemons=pokemons)
