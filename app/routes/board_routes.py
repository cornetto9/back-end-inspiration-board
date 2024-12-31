from flask import Blueprint, request, jsonify
from app import db
from ..models.board import Board 
import logging

board_routes = Blueprint('board_routes', __name__, url_prefix='/boards')

@board_routes.route('', methods=['GET'])
def get_boards():
    try:
        boards = Board.query.all()
        return jsonify([board.to_dict() for board in boards])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@board_routes.route('', methods=['POST'])
def create_board():
    try:
        data = request.json
        board = Board(title=data['title'], owner=data['owner'])
        db.session.add(board)
        db.session.commit()
        return jsonify(board.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

