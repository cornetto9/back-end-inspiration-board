from flask import Blueprint, request
from app.models.board import Board
from app.db import db
from .route_utilities import create_model

bp = Blueprint("board_bp", __name__, url_prefix="/boards")

@bp.post("")
def create_board(): 
    request_body = request.get_json()
    return create_model(Board, request_body)