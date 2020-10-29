from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>LSTM model </h1>'

@app.route('/generation-forecast')
def g_forecast():
    return '<h1>LSTM Energy generation forecast </h1>'

@app.route('/capacity-forecast')
def c_forecast():
    return '<h1>LSTM Energy capacity forecast </h1>'


if __name__ == '__main__':
    app.run(port='6600')
