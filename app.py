from flask import Flask, jsonify, abort, request, render_template
import threading
import time
import os
from flask_cors import CORS, cross_origin
from newbotlogic import super_rando, shmirator, switcher_func

app = Flask(__name__)
CORS(app)

@app.route("/message/", methods=['GET'])
def hello():
    text = request.args['message']
    ip = request.remote_addr

    return jsonify({'message': switcher_func(text,ip)})

def flask_thread():
    local = '127.0.0.1'
    heroku = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=heroku, port=port, use_reloader=False)

if __name__ == "__main__":
    thread1 = threading.Thread(target=flask_thread)
    thread1.start()