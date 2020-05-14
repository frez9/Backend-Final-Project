import json
from flask import Flask, request
import dao
from db import db

app = Flask(__name__)
db_filename = "eventbrite.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


@app.route('/api/events/', methods=['GET'])
def get_events():
    return success_response(dao.get_all_events())

@app.route('/api/events/', methods=['POST'])
def create_event():
    body = json.loads(request.data)
    event = dao.create_event(
        name=body.get('name'),
        description=body.get('description'),
        location=body.get('location'),
        date=body.get('date')
    )
    return success_response(event, 201)

@app.route('/api/events/<event_id>/', methods=['GET'])
def get_event(event_id):
    event = dao.get_event_by_id(event_id)
    if event is None:
        return failure_response("Event not Found!")
    return success_response(event)

@app.route('/api/events/<event_id>/', methods=['DELETE'])
def delete_event(event_id):
    event = dao.delete_event_by_id(event_id)
    if event is None:
        return failure_response("Event not Found!")
    return success_response(event)

@app.route('/api/events/<event_id>/review/', methods=['POST'])
def create_review(event_id):
    event = dao.get_event_by_id(event_id)
    if event is None:
        return failure_response("Event not found!")
    body = json.loads(request.data)
    review = dao.create_review(
        reviewer_name=body.get('reviewer_name'),
        title=body.get('title'),
        description=body.get('description'),
        rating=body.get('rating'),
        event_id= event_id
    )
    return success_response(review, 201)

@app.route('/api/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        name=body.get('name'),
        username=body.get('username')
    )
    return success_response(user, 201)

@app.route('/api/users/<user_id>/', methods=['GET'])
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not Found!")
    return success_response(dao.get_user_by_id(user_id))

@app.route('/api/events/<event_id>/add/', methods=['POST'])
def assign_user(event_id):
    body = json.loads(request.data)
    type = body.get('type')
    user_id = body.get('user_id')
    event = dao.get_event_by_id(event_id)
    user = dao.get_user_by_id(body.get('user_id'))
    new_user = dao.assign_user(
        user_id=body.get('user_id'),
        type=body.get('type'),
        event_id=event_id
    )
    if event is None:
        return failure_response("Event not found!")
    if user is None:
        return failure_response("User not found!")

    return success_response(event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
