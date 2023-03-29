from flask import Flask
import soduku

app = Flask(__name__)


@app.route('/')
def hello():
    pass
