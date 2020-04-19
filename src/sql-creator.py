from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

POSTGRES_URL = 'localhost:5432'
POSTGRES_USER = 'student'
POSTGRES_PW = 'parola'
POSTGRES_DB = 'db'

DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB
)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    surname = db.Column(db.String(30), unique=False, nullable=False)
    # address = db.


if __name__ == '__main__':
    db.create_all()
