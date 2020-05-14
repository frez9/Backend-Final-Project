# Backend-Final-Project

##### A basic events and tickiting API similar to stubhub. <br> IP Address: [35.231.29.81](http://35.231.29.81)


### Expected Functionality

##### *Values wrapped in `< >` are placeholders for what the field values should be*

#### **Get all events**

`GET` `/api/events/`
###### Response
```
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "Cooking with Gina",
            "description": "Watch as the award-winning chef, Gina, recreates popular dishes",
            "location": "Online",
            "date": 06222020,
            "reviews": [ <SERIALIZED REVIEW WITHOUT EVENT FIELD>, ... ],
            "organizers": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ],
            "attendees": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ]
        },
        {
            "id": 2,
            "name": "Working out during Quarantine",
            "description": "Learn the best and most-effective workouts you can do from home!",
            "location": "Online",
            "date": 05102020,
            "reviews": [ <SERIALIZED REVIEW WITHOUT EVENT FIELD>, ... ],
            "organizers": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ],
            "attendees": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ]
        }
        ...
    ]
}
```
#### **Create an event**

`POST` `/api/events/`
###### Request
```
{
    "name": <USER INPUT>,
    "description": <USER INPUT>,
    "location": <USER INPUT>,
    "description": <USER INPUT>,
    "date": <USER INPUT> // (mmddyyyy)
}
```
###### Response
```
{
    "success": true,
    "data": {            
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "description": <USER INPUT FOR DESCRIPTION>,
        "location": <USER INPUT FOR LOCATION>,
        "date": <USER INPUT FOR DATE>,
        "reviews": [],
        "organizers": [],
        "attendees": []
    }
}
```
#### **Get a specific event**

`GET` `/api/events/{id}/`
###### Response
```
{
    "success": true,
    "data": {            
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "description": <USER INPUT FOR DESCRIPTION>,
        "location": <USER INPUT FOR LOCATION>,
        "date": <USER INPUT FOR DATE>,
        "reviews": [ <SERIALIZED REVIEW WITHOUT EVENT FIELD>, ... ],
        "organizers": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ],
        "attendees": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ]
    }
}
```

#### **Delete a specific event**

`DELETE` `/api/events/{id}/`
###### Response
```
{
    "success": true,
    "data": {            
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "description": <USER INPUT FOR DESCRIPTION>,
        "location": <USER INPUT FOR LOCATION>,
        "date": <USER INPUT FOR DATE>,
        "reviews": [ <SERIALIZED REVIEW WITHOUT EVENT FIELD>, ... ],
        "organizers": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ],
        "attendees": [ <SERIALIZED USER WITHOUT EVENT FIELD>, ... ]
    }
}
```

#### **Create a user**

`POST` `/api/users/`
###### Request
```
{
    "name": <USER INPUT>,
    "username": <USER INPUT>
}
```
###### Response
```
{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "username": <USER INPUT FOR USERNAME>,
        "events": []
    }
}
```
#### **Get a specific user**

`GET` `/api/users/{id}/`
###### Response
```
{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "username": <USER INPUT FOR USERNAME>,
        "events": [ <SERIALIZED EVENT>, ... ]
    }
}
```
#### **Add a user to an event**

`POST` `/api/events/{id}/add/`
###### Request
```
{
    "user_id": <USER INPUT>,
    "type": "attendee" or "organizer"
}
```
###### Response
```
{
    "success": true,
    "data": <SERIALIZED EVENT>
}
```
#### **Create a review for an event**

`GET` `/api/events/{id}/review/`
###### Request
```
{
    "reviewer_name": <USER INPUT>,
    "title": <USER INPUT>,
    "description": <USER INPUT>,
    "rating": <USER INPUT>, // integer
    "event_id": <USER INPUT>
}
```
###### Response
```
{
    "success": true,
    "data": {
        "id": 0,
        "reviewer_name": "John Smith",
        "title": "Awesome event!",
        "description": "I had a wonderful time during this event! I met a lot of cool people!",
        "rating": 5,
        "event": {
            "id": 2,
            "name": "Working out during Quarantine",
            "description": "Learn the best and most-effective workouts you can do from home!",
            "location": "Online",
            "date": 05102020
        }
    }
}
```
