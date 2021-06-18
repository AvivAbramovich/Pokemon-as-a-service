import argparse

from flask import Flask


app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/api"


@app.route('/', methods=['PUT', 'POST'])
def create_pokemon():
    raise NotImplementedError()


@app.route('/autocomplete/<query>')
def autocomplete(query):
    raise NotImplementedError()
