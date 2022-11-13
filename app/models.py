from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())

    tasks = db.relationship('Task', backref='project')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)

    tasks = db.relationship('Task', backref='user')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    description = db.Column(db.String(), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime)
    week = db.Column(db.Integer)

    def __repr__(self):
        return "<Task for user '{}, in project {}, decription: {} for {} hours'>".format(self.user, self.project, self.description, self.hours)


