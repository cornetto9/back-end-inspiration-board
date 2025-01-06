from app.models.card import Card
from app.models.board import Board
from app.db import db
import pytest


def test_post_card_to_board(client, one_board):
    # Act
    response = client.post(
        f"/boards/1/cards",
        json={
            "message": "New Card",
            "likes_count": 5
        }
    )
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body["card"] == {
        "card_id": 1, 
        "message": "New Card",
        "likes_count": 5,
        "board_id": 1
    }

def test_post_card_to_board_board_not_found(client):
    # Act
    response = client.post(
        f"/boards/1/cards",
        json={
            "message": "New Card",
            "likes_count": 5
        }
    )
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board id 1 is not found"}

def test_post_card_to_board_likes_count_missing(client, one_board):
    # Act
    response = client.post(
        f"/boards/1/cards", json={"message": "New Card"}
    )
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == {"details": "Invalid data"}

def test_post_card_to_board_message_missing(client, one_board):
    # Act
    response = client.post(
        f"/boards/1/cards", json={"likes_count": 5}
    )
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == {"details": "Invalid data"}
    
def test_delete_card(client, one_card):
    # Act
    response = client.delete(f"/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Card deleted"}

def test_delete_card_not_found(client):
    # Act
    response = client.delete(f"/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Card id 1 is not found"}

def test_increment_card_likes_by_1(client, one_card):
    # Act
    response = client.patch(f"/cards/1/like")

    # Assert
    updated_card = db.session.get(Board, 1).cards[0]
    assert response.status_code == 204
    assert updated_card.likes_count == 11

def test_increment_card_likes_by_1_card_not_found(client):
    # Act
    response = client.patch(f"/cards/200/like")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Card id 200 is not found"}