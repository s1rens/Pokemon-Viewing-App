from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route("/")
def home_page():
  return render_template('index.html', number=random.randrange(0,10))

@app.route("/pokemon")
def pokemon():
  pokeInput = request.args['pokeInput']
  pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokeInput).json()
  print(pokemon['sprites'])
  return render_template('pokemon.html', pokemon=pokemon)


# No need to bother with anything below this
if __name__ == "__main__":
  app.run()
