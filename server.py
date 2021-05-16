# env FLASK_APP=server.py flask run --host=0.0.0.0 --port=5013
from flask import Flask, request
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app)

def cleanStr(str, joinStr):
    return joinStr.join(re.findall("[0-9a-zA-Z]+", str))

@app.route('/')
def index():
    return ''

@app.route('/publish', methods=['POST'])
def drawRow():
    data = request.get_json(force=True)
    params = {
        'topic': data.get('topic'),
        'message': data.get('message')
    }

    topic = cleanStr(params['topic'], '/')
    message = cleanStr(params['message'], ' ')

    str = f"""mosquitto_pub -t {topic} -m \"{message}\""""
    print(str)
    os.system(str)
    return ('', 204)
  
