import os.path
import json
import logging

from flask import Flask, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

from paas.bl import PokemonBL, NotValidPokemonError
from paas.dal.es_dal import ESPokemonDAL


app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(
    Response('Not Found', status=404),
    {'/api': app.wsgi_app}
)

with open(os.path.join(os.path.dirname(__file__), 'pokemon_schema.json')) as f:
    bl = PokemonBL(json.load(f), ESPokemonDAL())

# check everything is ok before begin
try:
    bl.health()
except Exception as e:
    logging.error(f'Health check failed: %s', str(e))
    exit(1)


@app.route('/', methods=['PUT', 'POST'])
def create_pokemon():
    if request.content_type != 'application/json':
        return 400, 'expecting json'
    content = request.json
    try:
        bl.index_pokemon(content)
        return 'OK', 200
    except NotValidPokemonError as e:
        return 400, str(e)


@app.route('/autocomplete/<query>')
def autocomplete(query):
    results = bl.query(query)
    data = [p.as_dict() for p in results]
    return Response(json.dumps(data), mimetype='application/json')


if __name__ == '__main__':
    app.run()
