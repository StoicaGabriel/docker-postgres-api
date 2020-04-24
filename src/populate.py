from src.sql_creator import create_all_tables, drop_all_tables, db
from src.sql_creator import User, Student, Professor, Discipline, Schedule, StudyClass

if __name__ == '__main__':
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

    # Create some schedules and insert them into table

    # Create some study classes and insert them into table

    # Create some students and insert them into table

    # Create some disciplines and insert them into table

    # Update some, then delete some and query some tables (maybe separate functions)
