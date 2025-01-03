from app.models.card import Card
from app.db import db
import pytest


def test_get_cards_no_cards_added(client):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == {"card": []}


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

def test_delete_card(client, one_card):
    # Act
    response = client.delete(f"/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Card deleted"}

def test_update_card_likes(client, one_card):
    # Act
    response = client.put(f"/cards/1", json={"likes_count": 20})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["card"]["likes_count"] == 20