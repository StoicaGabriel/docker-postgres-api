import json
import random
from src.sql_creator import create_all_tables, drop_all_tables, db
from src.sql_creator import User, Student, Professor, Discipline, Schedule, StudyClass

if __name__ == '__main__':
    random.seed(a=2)

    drop_all_tables()
    create_all_tables()

    # Create some users and insert them into the table
    admin = User(username="admin", email="johndoe@example.com")
    guest = User(username="guest", email="guest@example.com")
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    # TODO (in this exact order):

    # Create some professors and insert them into table

    prof1 = Professor(name='Popescu', surname='Marin', merits='Prof. dr. Ing.')
    prof2 = Professor(name='George', surname='Alexandru', merits='Conf. dr. Ing.')
    prof3 = Professor(name='Popescu', surname='Andrei', merits='S.I. dr. Ing.')

    db.session.add(prof1)
    db.session.add(prof2)
    db.session.add(prof3)
    db.session.commit()

    # Create some schedules and insert them into table
    schedule_data_dict = {
        "Luni": {
            "8:00-10:00": "BD-curs (P. Marin)",
            "10:00-12:00": "IM-lab (G. Alexandru)",
            "12:00-14:00": "BD-sem (P. Marin)",
        },
        "Marti": {
            "8:00-12:00": "IM-lab (G. Alexandru)",
            "12:00-14:00": "DE-sem (P. Andrei)",
        },
        "Miercuri": {
            "8:00-10:00": "DE-curs (P. Andrei)",
            "12:00-14:00": "DE-lab (P. Andrei)",
        },
        "Joi": {
            "8:00-12:00": "IM-curs (G. Alexandru)",
        },
        "Vineri": {

        },
    }
    schedule_data = json.dumps(schedule_data_dict)

    schedule = Schedule(schedule=schedule_data)
    db.session.add(schedule)
    db.session.commit()

    # Create some study classes and insert them into table
    # By default, a class cannot be formed in the absence of a schedule

    study_class = StudyClass(
        name="1-A",
        year_of_study="1L",
        schedule_id=1,
        professor_id=3,
    )

    db.session.add(study_class)
    db.session.commit()

    # Create some students and insert them into table

    for i in range(100):
        name = "Student" + str(i + 1)
        surname = "Student" + str(i + 1)
        address = "Street. " + str(i + random.randint(1, 30)) + \
                  " City " + str(random.randint(1, 15))
        year_of_study = "1L"
        # Nothing under 50/100 should be present in the db as adm_score
        adm_score = random.randint(15, 30) / 30 * 100
        scores_dict = {
            "BD": None,
            "DE": None,
            "Imagistica": None,
        }
        scores = json.dumps(scores_dict)
        study_class_id = 1

        student = Student(
            name=name,
            surname=surname,
            address=address,
            year_of_study=year_of_study,
            adm_score=adm_score,
            scores=scores,
            study_class_id=study_class_id,
        )
        db.session.add(student)
    db.session.commit()

    # Create some disciplines and insert them into table
    de = Discipline(
        name="Dispozitive electronice-DE",
        course_schedule="Miercuri 8:00-10:00",
        seminary_schedule="Marti 12:00-14:00",
        lab_schedule="Miercuri 12:00-14:00",
        schedule_id=1,
        study_class_id=1,
        professor_id=3,
    )
    bd = Discipline(
        name="Baze de date-BD",
        course_schedule="Luni 8:00-10:00",
        seminary_schedule="Luni 12:00-14:00",
        lab_schedule=None,
        schedule_id=1,
        study_class_id=1,
        professor_id=1,
    )
    imagistica = Discipline(
        name="Imagistica-IM",
        course_schedule="Joi 8:00-12:00",
        seminary_schedule=None,
        lab_schedule="Luni 10:00-12:00, Marti 8:00-12:00",
        schedule_id=1,
        study_class_id=1,
        professor_id=2,
    )

    db.session.add(de)
    db.session.add(bd)
    db.session.add(imagistica)
    db.session.commit()

    # Update some, then delete some and query some tables (maybe separate functions)
