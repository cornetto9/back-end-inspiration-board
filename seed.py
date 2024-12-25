from app import create_app, db
from app.models.card import Card
from app.models.board import Board

from dotenv import load_dotenv
load_dotenv()

my_app = create_app()
with my_app.app_context():
    db.create_all()

    # Create sample boards
    board1 = Board(title="My First Board", owner="Me")
    board2 = Board(title="Motivation Quotes", owner="Ada Lovelace")
    board3 = Board(title="Daily Affirmations", owner="Grace Hopper")
    board4 = Board(title="Coding Tips", owner="Katherine Johnson")
    
    db.session.add_all([board1, board2, board3, board4])
    db.session.commit()

    # Create sample cards
    cards = [
        Card(message="Never give up!", likes_count=5, board_id=2),
        Card(message="You are capable of amazing things", likes_count=10, board_id=2),
        Card(message="I am becoming a better programmer every day", likes_count=3, board_id=3),
        Card(message="Debug with patience", likes_count=7, board_id=4),
        Card(message="Remember to take breaks", likes_count=15, board_id=4),
        Card(message="Start small, think big", likes_count=8, board_id=3)
    ]
    
    db.session.add_all(cards)
    db.session.commit()