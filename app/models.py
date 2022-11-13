from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())

    tasks = db.relationship('Task', backref='project')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    # project = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime)
    week = db.Column(db.Integer)

    def __repr__(self):
        return "<Task for user '{}, in project {}, decription: {} for {} hours'>".format(self.user, self.project, self.description, self.hours)


