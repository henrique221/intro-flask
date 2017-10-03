# coding: utf-8

from flask import Flask
from db import noticias

app = Flask(__name__)

@app.route("/noticias/cadastro/")
def index():
    return "teste"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
