#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_tasks():
    return jsonify({'message': message}) #TODO: how to get message

if __name__ == '__main__':
    app.run(debug=True)