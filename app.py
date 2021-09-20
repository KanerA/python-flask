import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson.json_util import dumps

load_dotenv()
app = Flask(__name__)
uri = os.getenv("MONGO_URI")

app.config["MONGO_URI"] = uri
mongo = PyMongo(app)


def parse_json(data):
    json_str = dumps(data)
    return json_str


@app.route("/paste/get", methods=["GET"])
def pastes():
    data = mongo.db.pastes.find({})
    array = list(data)
    dataArr = []
    for i in range(data.count()):
        parsed = parse_json(array[i])
        dataArr.append(parsed)
    return jsonify(dataArr)


if __name__ == "__main__":
    app.run(debug=False)
