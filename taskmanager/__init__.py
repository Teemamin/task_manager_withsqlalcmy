import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] =  os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri.replace("posgres://", "posgresql://",1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


# instance of SQLAlchemy pass the instance of flask
db = SQLAlchemy(app)
db.init_app(app)

# need to have routes import after db and app to avoid circular import error
from taskmanager import routes #nqa

