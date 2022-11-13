from app import app, db
from app.models import User, Project, Task
import random, time
from datetime import datetime

names = ['Θεόδωρος Μπούσιος', 'Μαρία Χριστίδου', 'Γιάννης Πετρίδης', 'Ελένη Στεργίου', 'Πέτρος Ράλλης']
projects = ['ΕΜΔ', 'HowTo', 'eΚΕΠ', 'Ψηφιακά έγγραφα gov', 'Πλατφόρμα Αναπληρωτές']
descriptions = [
    'Write report', 'Create presentations', 'Webstite design',
    'Code developemnt', 'Server migration', 'Meeting with team',
    'Meeting with client', 'Test functionality'
]

n_tasks = 60

#random.seed(45)

def get_random_date():
    d = random.randint(int(time.time()) - 60 *24*60*60 , int(time.time()))
    return datetime.fromtimestamp(d)


# _, week_num, _ = get_random_date().isocalendar()




with app.app_context():

    db.drop_all()
    db.create_all()

    demo_projects = list()
    demo_users = list()

    for project in projects:
        row = Project(name=project,description='μια περιγραφή του project')
        db.session.add(row)
        demo_projects.append(row)
    db.session.commit()

    for name in names:
        firstname, lastname = name.split()
        row = User(firstname=firstname,lastname=lastname)
        db.session.add(row)
        demo_users.append(row)
    db.session.commit()

    for i in range(n_tasks):
        random_date = get_random_date()
        _, week, _= random_date.isocalendar()

        row = Task(
            user=random.choice(demo_users),
            project= random.choice(demo_projects),
            description = random.choice(descriptions),
            hours = random.choice(range(1, 10)),
            date = random_date,
            week = week
            )
        db.session.add(row)
    db.session.commit()




