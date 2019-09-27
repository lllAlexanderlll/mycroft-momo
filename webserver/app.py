#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_tasks():
    return "test"

if __name__ == '__main__':
    app.run(debug=True)