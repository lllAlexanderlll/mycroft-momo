#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

# CORS(app, support_credentials=True)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/message', methods=['GET'])
def get_message():
	message = ""
	with open('/opt/mycroft/skills/mycroft-momo/userMessage', 'r') as f:
		message = f.read()
	return message

if __name__ == '__main__':
    app.run(debug=True)
