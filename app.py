import flask
from flask import Flask, jsonify, render_template, redirect, url_for

import numpy as np
from DeepLearningUTSModel import DeepLearningUTSModel
from tensorflow.keras.models import load_model

LSTM_gen = load_model('output/LSTM_energy_gen.h5')
LSTM_cap = load_model('output/LSTM_energy_cap.h5')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("LSTM_home.html")

@app.route('/dataviz')
def data_viz(): 
    return render_template("data.html")

@app.route('/generation-forecast/<n_ahead>', methods=['GET', 'POST'])
def g_forecast(n_ahead):

    data = {"success": False}
    params = flask.request.json

    data['prediction'] = f"The prediction is {n_ahead} days in the future"

    ts = np.array(params.get("ts"))
    X, y = DeepLearningUTSModel.create_ts_sequences(series=ts, lag=2)
    data["response"] = LSTM_gen.predict(X).tolist()
    data["success"] = True

    return flask.jsonify(data)

@app.route('/capacity-forecast/<n_ahead>')
def c_forecast(n_ahead):
    return '<h1>LSTM Energy capacity forecast </h1>'


if __name__ == '__main__':
    app.run(debug=True,
            port='6600', host='0.0.0.0')

