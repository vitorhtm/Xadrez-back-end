from flask import Flask, request
from class_tab import Tabuleiro
from flask_cors import CORS

app = Flask("Hello world")
CORS(app)
tab = Tabuleiro()


@app.route("/olamundo", methods=["GET"])
def olamundo():
    return {"tabuleiro": tab.xadrez}


@app.route("/jogar", methods=["POST"])
def jogar():

    body = request.get_json()
    tab.jogar(**body)
    tab.exibir()
    return {"tabuleiro": tab.xadrez}

app.run()
