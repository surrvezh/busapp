from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transportapp.db'
db=SQLAlchemy(app)
from transportapp import route


