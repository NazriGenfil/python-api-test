from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes #import jalur

app = Flask(__name__)
api = Api(app)
Bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://'
}

initialize_db(app)
initialize_routes(api) #memanggil jalur

app.run(debug=True, port=5001)
