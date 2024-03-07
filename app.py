from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods = ['GET'])
@cross_origin()
def home_route():
    return {
        "message": "Hello"
    }