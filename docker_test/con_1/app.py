import json
import logging

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def get_hello():
    logging.debug("Connecting to other container...")
    # Issue with connecting...
    response = requests.get('http://127.0.0.1/8000')
    logging.debug("Printing...")
    return response.json()


@app.route('/test')
def test():
    string: str = "Working..."
    return json.dumps(string)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')
