import flask
from flask import Flask, jsonify

import numpy as np
from DeepLearningUTSModel import DeepLearningUTSModel
from tensorflow.keras.models import load_model

LSTM_gen = load_model('output/LSTM_energy_gen.h5')
LSTM_cap = load_model('output/LSTM_energy_cap.h5')

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>LSTM model </h1>'

@app.route('/generation-forecast', methods=['GET', 'POST'])
def g_forecast():

    data = {"success": False}
    params = flask.request.json

    
    ts = np.array(params.get("ts"))
    X, y = DeepLearningUTSModel.create_ts_sequences(series=ts, lag=2)
    data["response"] = LSTM_gen.predict(X).tolist()
    data["success"] = True

    return flask.jsonify(data)

@app.route('/capacity-forecast')
def c_forecast():
    return '<h1>LSTM Energy capacity forecast </h1>'


if __name__ == '__main__':
    app.run(port='6600', host='0.0.0.0')
