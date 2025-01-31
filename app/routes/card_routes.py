from flask import Blueprint, request, Response
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

@bp.patch("/<card_id>/like")
def update_likes(card_id):
    card = validate_model(Card, card_id)
    if card.likes_count is None:
        card.likes_count = 1
    else:
        card.likes_count += 1
    
    db.session.commit()
    return Response(status=204, mimetype="application/json")