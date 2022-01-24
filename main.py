#from hgtddb import app
#if __name__ == '__main__':
#	app.run(debug=False)

from flask.app import Flask
from app import main
#from database import Session
app = Flask(__name__)
app.register_blueprint(main)

#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    Session.remove()
app.run()