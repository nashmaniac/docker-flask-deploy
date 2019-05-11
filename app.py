from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(dict(message='Hello World'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
