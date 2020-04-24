from flask import Flask
from flask_sqlalchemy import SQLAlchemy

POSTGRES_URL = 'localhost:5432'
POSTGRES_USER = 'student'
POSTGRES_PW = 'parola'
POSTGRES_DB = 'db'

DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    db.init_app(app)
    return app
