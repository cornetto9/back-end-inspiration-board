from flask import abort, make_response, request
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError: 
        abort(make_response({"message":f"{cls.__name__} id {model_id} is invalid"}, 400))

    query = db.select(cls).where(cls.id == model_id) 
    model = db.session.scalar(query)

    if not model:
        abort(make_response({"message":f"{cls.__name__} id {model_id} is not found"}, 404))

    return model

def create_model(cls, model_data): 
    try: 
        new_model = cls.from_dict(model_data) 

    except KeyError as error: 
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))        

    db.session.add(new_model) 
    db.session.commit()

    return make_response({f"{cls.__name__.lower()}": new_model.to_dict()}, 201)