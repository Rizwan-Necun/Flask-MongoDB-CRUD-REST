from bson.objectid import ObjectId
from flask import Flask
from flask_pymongo import PyMongo
# from bson.json_utils import dumps
from bson import json_util
from bson import dumps
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Mongopoc1"

mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(debug=True)
