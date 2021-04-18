from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

app = Flask(__name__)
login = LoginManager(app)
api = Api(app)
api.app.config['RESTFUL_JSON'] = {"ensure_ascii": False}
app.config['SECRET_KEY'] = 'you-will-never-guess'