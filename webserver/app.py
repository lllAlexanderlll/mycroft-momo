#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_message():
	message = ""
	with open('/opt/mycroft/skills/mycroft-momo/newMessage', 'r') as f:
		message = f.read()
	response = flask.Response(message)
	response.headers['Access-Control-Allow-Origin'] = '*'
	return response

if __name__ == '__main__':
    app.run(debug=True)
