#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_message():
	message = ""
	with open('newMessage', 'r') as f:
		message = f.read()
    return message

if __name__ == '__main__':
    app.run(debug=True)