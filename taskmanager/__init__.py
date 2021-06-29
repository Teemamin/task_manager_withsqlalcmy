import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] =  os.environ.get("DB_URL")

# instance of SQLAlchemy pass the instance of flask
db = SQLAlchemy(app)
# need to have routes import after db and app to avoid circular import error
from taskmanager import routes #nqa

