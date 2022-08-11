from flask import Flask,request
from main import main

app = Flask(__name__)

@app.route('/')
def hello():
    key = request.args.get('key')
    return main(key)