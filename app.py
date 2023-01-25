from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from db import db
from flask_jwt_extended import JWTManager
from os import getenv
from datetime import timedelta

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config["JWT_SECRET_KEY"] = getenv('SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
jwt = JWTManager(app)

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Mi aplicacion con Flask :D"

import routers

# if __name__ == '__main__':
#     app.run(debug=True)