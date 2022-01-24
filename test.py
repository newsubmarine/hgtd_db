<<<<<<< HEAD
from flask import Flask 

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def hello_world():
    return "Hello world!"

app.run('127.0.0.1', port=5500)
=======
import config

cfg = config.ReadConfig("config.yaml")
print(cfg)

server = cfg['Server']
database = cfg['Database']
print(server['host'])
print("xxx")
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
