from flask import Flask
from model.sql_alchemy_db import db
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codecool.sqlite'
db.app = app
db.init_app(app)
print('przeszło')