from flask import Flask, request
from main import main

app = Flask(__name__)


@app.route('/')
def hello():
    key = request.args.get('key')
    if key is None:
        return 'Missing key'
    print(key)
    return main(key)


app.run(debug=True, port=5000)
