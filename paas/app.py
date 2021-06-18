import os.path
import json

from flask import Flask, request, make_response

from paas.bl import PokemonBL, PokemonBlError
from paas.dal.es_dal import ESPokemonDAL


app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/api"

with open(os.path.join(os.path.dirname(__file__), 'pokemon_schema.json')) as f:
    bl = PokemonBL(json.load(f), ESPokemonDAL())


@app.route('/', methods=['PUT', 'POST'])
def create_pokemon():
    content = request.json
    try:
        bl.index_pokemon(content)
    except PokemonBlError as e:
        raise NotImplementedError()


@app.route('/autocomplete/<query>')
def autocomplete(query):
    raise NotImplementedError()
