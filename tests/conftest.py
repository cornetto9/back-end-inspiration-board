import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.board import Board
from app.models.card import Card

load_dotenv()

# @pytest.fixture
# def app():
#     # create the app with a test configuration
#     test_config = {
#         "TESTING": True,
#         "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
#     }
#     app = create_app(test_config)

#     @request_finished.connect_via(app)
#     def expire_session(sender, response, **extra):
#         db.session.remove()

#     with app.app_context():
#         db.create_all()
#         yield app

#     # close and remove the temporary database
#     with app.app_context():
#         db.drop_all()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_board(app):
    new_board = Board(title="Software Developer", owner="Homer J Simpson")
    db.session.add(new_board)
    db.session.commit()

# @pytest.fixture
# def one_card(app):
#     new_card = Card(message="Build a FullStack App", 
#                     likes=10)
#     db.session.add(new_card)
#     db.session.commit()

@pytest.fixture
def one_card(app, one_board):
    new_card = Card(message="Build a FullStack App", likes_count=10, board_id=1)
    db.session.add(new_card)
    db.session.commit()


@pytest.fixture
def three_boards(app):
    boards = [
        Board(title="Board 1", owner="Owner 1"),
        Board(title="Board 2", owner="Owner 2"),
        Board(title="Board 3", owner="Owner 3")
    ]
    db.session.add_all(boards)
    db.session.commit()