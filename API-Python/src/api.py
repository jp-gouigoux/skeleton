from flask import Flask
from flask import make_response
from flask import request

import requests, json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():

    print "Entering /test method"

    response = make_response("Test OK")
    response.mimetype = 'application/json'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
