#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, abort, Response
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file("index.html")
    
@app.errorhandler(404)
def not_found_error(error):
    return app.send_static_file("404.html"), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    