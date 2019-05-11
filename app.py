from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(dict(message='Hello World'))

@app.route('/home')
def hello_home():
    return jsonify(dict(message='Hello Home'))

@app.route('/about')
def hello_about():
    return jsonify(dict(message='Hello About'))

@app.route('/final')
def hello_final():
    return jsonify(dict(message='Final Route added'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
