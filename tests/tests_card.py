from app.models.card import Card
from app.db import db
import pytest

def test_post_card_to_board(client, one_board):
    # Act
    response = client.post("/boards/1/cards", json={
        "message": "All you can do is try"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "message": "All you can do is try"
    }