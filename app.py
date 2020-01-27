from flask import Flask, jsonify, abort, request, render_template
import threading
import time
import os
from flask_cors import CORS, cross_origin
from newbotlogic import super_rando

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def hello():
    text = request.args['message']
    ip = request.remote_addr

    return jsonify(super_rando(text))



if __name__ == "__main__":
    local = '127.0.0.1'
    heroku = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=heroku, port=port)
