import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


if __name__ == "__main__":
    app.run(debug=False)
