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
    address = db.Column(db.String(200), unique=False, nullable=True)
    year_of_study = db.Column(db.String(2), unique=False, nullable=True)
    adm_score = db.Column(db.Float, unique=False, nullable=False)
    # Current exam scores for all past years and semesters
    scores = db.Column(db.String(200), unique=False, nullable=True)
    # Foreign key to a StudyClass instance
    study_class = db.Column(db.Integer, db.ForeignKey('st_class.id'))

    # Foreign key relationship
    st_class = db.relationship('StudyClass', backref=db.backref('students', lazy=True))


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    surname = db.Column(db.String(30), unique=False, nullable=False)
    # Rank of the teacher eg. PhD...
    merits = db.Column(db.String(10), unique=False, nullable=False)
    study_classes = db.Column()  # TODO: vector type which links to multiple StudyClass objects


class StudyClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    year_of_study = db.Column(db.String(2), unique=False, nullable=False)
    schedule = db.Column(db.Integer, db.ForeignKey('sc'))

    sc = db.relationship('Schedule', backref=db.backref('classes', lazy=True))


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # This is where the schedule is written for every week's day
    schedule = db.Column(db.String(200), unique=False, nullable=True)


# Not implemented, TBD if needs to be added
# class Discipline(db.Model):
#     id = db.Column
#     # Name is unique, tough multiple teachers can be assigned for different classes
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     # Day of the week + hour interval of the class
#     course_schedule = db.Column(db.String(20), unique=False, nullable=True)
#     lab_schedule = db.Column(db.String(20), unique=False, nullable=True)
#     seminary_schedule = db.Column(db.String(20), unique=False, nullable=True)


if __name__ == '__main__':
    db.create_all()
