from db import db, Event, Review, Attendee, Organizer, User

def get_all_events():
    return [x.serialize() for x in Event.query.all()]

def create_event(name, description, location, date):
    new_event = Event(
        name=name,
        description=description,
        location=location,
        date=date
    )

    db.session.add(new_event)
    db.session.commit()
    return new_event.serialize()

def get_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    return event.serialize()

def delete_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    db.session.delete(event)
    db.session.commit()
    return event.serialize()

def create_review(reviewer_name, title, description, rating, event_id):
    new_review = Review(
        reviewer_name=reviewer_name,
        title=title,
        description=description,
        rating=rating,
        event_id=event_id
    )
    db.session.add(new_review)
    db.session.commit()
    return new_review.serialize()

def create_user(name, username):
    new_user = User(
        name=name,
        username=username
    )

    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    if user is not None:
        return user.serialize()
    attendee = Attendee.query.filter_by(id=id).first()
    if attendee is not None:
        return attendee.serialize()
    organizer = Organizer.query.filter_by(id=id).first()
    if organizer is not None:
        return organizer.serialize()

def assign_user(event_id, user_id, type):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None

    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        if type == 'attendee':
            name = user.name
            username = user.username
            attendee = Attendee(
                name=name,
                username=username,
            )
            event.attendees.append(attendee)
            db.session.commit()
            db.session.delete(user)
            db.session.commit()
            return event.serialize()

        if type == 'organizer':
            name = user.name
            username = user.username
            organizer = Organizer(
                name=name,
                username=username,
            )
            event.organizers.append(organizer)
            db.session.commit()
            db.session.delete(user)
            db.session.commit()
            return event.serialize()

    attendee = Attendee.query.filter_by(id=user_id).first()
    if attendee is not None:
        if type == 'attendee':
            name = attendee.name
            username = attendee.username
            attendee = Attendee(
                name=name,
                username=username,
            )
            event.attendees.append(attendee)
            db.session.commit()
            db.session.commit()
            return event.serialize()

        if type == 'organizer':
            name = attendee.name
            username = attendee.username
            organizer = Organizer(
                name=name,
                username=username,
            )
            event.organizers.append(organizer)
            db.session.commit()
            db.session.commit()
            return event.serialize()

    organizer = Organizer.query.filter_by(id=user_id).first()
    if organizer is not None:
        if type == 'attendee':
            name = organizer.name
            username = organzier.username
            attendee = Attendee(
                name=name,
                username=username,
            )
            event.attendees.append(attendee)
            db.session.commit()
            db.session.commit()
            return event.serialize()

        if type == 'organizer':
            name = organizer.name
            username = organizer.username
            organizer = Organizer(
                name=name,
                username=username,
            )
            event.organizers.append(organizer)
            db.session.commit()
            db.session.commit()
            return event.serialize()

    return None
