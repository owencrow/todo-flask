from flask import Flask, request, jsonify
from service import ToDoService
from models import Schema

import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name + "!"


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
