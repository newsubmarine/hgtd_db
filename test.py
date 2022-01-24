from flask import Flask 

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def hello_world():
    return "Hello world!"

app.run('127.0.0.1', port=5500)