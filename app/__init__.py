import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Set a project base directory variable
baseDir = os.path.abspath(os.path.dirname(__file__))


# create the extension
db = SQLAlchemy()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'
# configure the SQLite database, relative to the app instance folder
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(baseDir, 'database.sqlite')

# initialize the app with the extension
db.init_app(app)



from app import routes

