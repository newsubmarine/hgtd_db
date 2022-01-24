from . import main
import json
@main.route('/helloworld')
def hello():
    return (json.dumps({ 'message': "Hello friend!" }), 
        200, { 'content_type': 'application/json'})


