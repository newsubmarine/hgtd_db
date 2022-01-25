## Flask application 

import os
import click
from flask_bootstrap import Bootstrap

from app import create_app

from Root.database import Session
#from database import Session
app = create_app()
bootstrap = Bootstrap(app)

@app.teardown_appcontext
def teardown_db(exception=None):
    Session.remove()

app.run(debug=True)

