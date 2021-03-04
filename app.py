from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from cli import register

from api.models.db import init_db
from flask_restful import Api
from api.resources.errors import errors

app = Flask(__name__)
app.config.from_object('config.ProductionConf')

mail = Mail(app)
from api.routes.routes import init_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

init_db(app)
init_routes(api)

# Register application's custom command-line commands
register(app)