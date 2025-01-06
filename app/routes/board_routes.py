from flask import Blueprint, request
from app.models.board import Board
from app.models.card import Card
from app.db import db
from .route_utilities import create_model, validate_model, get_models_with_filters

bp = Blueprint("board_bp", __name__, url_prefix="/boards")

@bp.post("")
def create_board(): 
    request_body = request.get_json()
    return create_model(Board, request_body)

@bp.get("")
def get_all_boards():
    return get_models_with_filters(Board, request.args)

@bp.get("/<board_id>")
def get_board(board_id):
    board = validate_model(Board, board_id)

    return {"board": board.to_dict()}, 200

@bp.get("/<board_id>/cards")
def get_cards_by_board(board_id):
    board = validate_model(Board, board_id)

    return {"cards": [card.to_dict() for card in board.cards]}, 200

@bp.post("/<board_id>/cards")
def create_card_within_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()

    # check if board_id is in request body and if it is the same as the board_id in the URL
    if 'board_id' in request_body:
        request_board_id = int(request_body['board_id'])
        if request_board_id != board.board_id:
            return {"message": f"Board ID in URL {board_id} must match board_id in request body {request_board_id}"}, 400
    request_body['board_id'] = board.board_id
    return create_model(Card, request_body)

@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    
    # Delete all cards associated with the board
    for card in board.cards:
        db.session.delete(card)
    
    db.session.delete(board)
    db.session.commit()
    
    return {"message": f"Board {board_id} and its cards have been deleted"}, 200