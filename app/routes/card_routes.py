from flask import Blueprint, request
from app.models.board import Board
from app.models.card import Card
from app.db import db
from .route_utilities import create_model, validate_model, get_models_with_filters

bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return {"message": "Card deleted"}, 200

@bp.put("/<card_id>")
def update_card_likes(card_id):
    card = validate_model(Card, card_id)
    request_body = request.get_json()
    card.likes_count = request_body['likes_count']
    db.session.commit()
    return {"card": card.to_dict()}, 200

