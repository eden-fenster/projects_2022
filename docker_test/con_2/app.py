import json
import logging

import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    logging.debug("Sending request...")
    requests.get('http://127.0.0.1:3000/test')
    hi: str = "Hello World"
    return json.dumps(hi)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')