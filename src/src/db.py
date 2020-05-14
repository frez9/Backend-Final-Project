from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table1 = db.Table('association1', db.Model.metadata,
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('attendee_id', db.Integer, db.ForeignKey('attendee.id'))
)

association_table2 = db.Table('association2', db.Model.metadata,
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('organizer_id', db.Integer, db.ForeignKey('organizer.id'))
)

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    reviews = db.relationship('Review', cascade='delete')
    organizers = db.relationship('Organizer', secondary=association_table2, back_populates='events')
    attendees = db.relationship('Attendee', secondary=association_table1, back_populates='events')

    def __init(self, **kwargs):
        self.name = kwargs.get('name','')
        self.description = kwargs.get('description','')
        self.location = kwargs.get('location','')
        self.date = kwargs.get('date','')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'date': self.date,
            'reviews': [x.serialize() for x in self.reviews],
            'organizers': [y.serialize() for y in self.organizers],
            'attendees': [z.serialize() for z in self.attendees]
        }

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    reviewer_name = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __init__(self, **kwargs):
        self.reviewer_name = kwargs.get('reviewer_name','')
        self.title = kwargs.get('title', '')
        self.description = kwargs.get('description', '')
        self.rating = kwargs.get('rating', '')
        self.event_id = kwargs.get('event_id')

    def serialize(self):
        return {
            'id': self.id,
            'reviewer_name': self.reviewer_name,
            'title': self.title,
            'description': self.description,
            'rating': self.rating,
            'event': self.event_id,
        }

class Attendee(db.Model):
    __tablename__ = 'attendee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    events = db.relationship('Event', secondary=association_table1, back_populates='attendees')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.username = kwargs.get('username','')

    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'username': self.username,
        }

class Organizer(db.Model):
    __tablename__ = 'organizer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    events = db.relationship('Event', secondary=association_table2, back_populates='organizers')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.username = kwargs.get('username','')

    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'username': self.username,
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.username = kwargs.get('username','')

    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'username': self.username,
        'events': []
        }
