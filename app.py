from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import math

prices={"gold":6.800,"silver":.073,"palladium":3.380,"platinum":2.400,"copper":0.00074}

model = pickle.load(open("Model/mobile1.pkl", 'rb'))

app = Flask(__name__)
cors = CORS(app)
    
@app.route('/api', methods = ['POST'])
@cross_origin()
def predict():
    data = request.get_json()
    weight = float(data['weight'])
    try:
        prediction = model.predict([[weight]])
        gold = int(prediction) * 0.0003 * 1000
        silver = int(prediction) * 0.001 * 1000
        palladium = int(prediction) * 0.0002 * 1000
        platinum = int(prediction) * 0.0001 * 1000
        copper = int(prediction) * 0.40 * 1000
        
        gold1 = math.ceil(gold * prices.get("gold") / 2)
        silver1 = math.ceil((silver * prices.get("silver") / 5))
        palladium1 = math.ceil((palladium * prices.get("palladium") / 5))
        platinum1 = math.ceil((platinum * prices.get("platinum") / 5))
        copper1 = math.ceil((copper * prices.get("copper") / 5))
        total_credit_points = (gold1 + silver1 + palladium1 + platinum1 + copper1)
        return jsonify({
            "Credit Score" : int(total_credit_points),
            "Gold" : gold,
            "Silver" : silver,
            "Copper" : copper,
            "Palladium" : palladium,
            "Platinum" : platinum
        })
    except Exception as e:
        return e