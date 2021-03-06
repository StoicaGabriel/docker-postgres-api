from src.app import db, create_app

app = create_app()
app.app_context().push()


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
    study_class_id = db.Column(db.Integer, db.ForeignKey('study_class.id'))

    # Foreign key relationship
    study_class = db.relationship('StudyClass', backref=db.backref('students', lazy=True))

    def __repr__(self):
        return f'{self.name} {self.surname} {self.address} {self.adm_score} {self.scores}'


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    surname = db.Column(db.String(30), unique=False, nullable=False)
    # Rank of the teacher eg. PhD...
    merits = db.Column(db.String(20), unique=False, nullable=False)

    # Relationship for foreign key in a different table
    study_classes = db.relationship('StudyClass', backref='professor')
    discipline = db.relationship('Discipline', backref='professor')

    def __repr__(self):
        return f'{self.merits} {self.name} {self.surname}'


class StudyClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    year_of_study = db.Column(db.String(2), unique=False, nullable=False)

    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))

    schedule = db.relationship('Schedule', backref=db.backref('classes', lazy=True))
    discipline = db.relationship('Discipline', backref='study_class')

    def __repr__(self):
        return f'{self.name} {self.year_of_study}'


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # This is where the schedule is written for every week's day
    schedule = db.Column(db.String(1000), unique=False, nullable=True)

    disciplines = db.relationship('Discipline', backref='schedule')

    def __repr__(self):
        return f'{self.schedule}'


class Discipline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    # Day of the week + hour interval of the class
    course_schedule = db.Column(db.String(50), unique=False, nullable=True)
    lab_schedule = db.Column(db.String(50), unique=False, nullable=True)
    seminary_schedule = db.Column(db.String(50), unique=False, nullable=True)

    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'))
    study_class_id = db.Column(db.Integer, db.ForeignKey('study_class.id'))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))

    def __repr__(self):
        return f'{self.name} {self.course_schedule} {self.lab_schedule} {self.seminary_schedule}'


def create_all_tables():
    db.create_all()


def drop_all_tables():
    db.drop_all()
