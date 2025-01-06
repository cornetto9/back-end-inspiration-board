from app.models.board import Board
from app.db import db
import pytest

def test_get_board_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == {"board": []}

def test_get_boards_one_saved_boards(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {
        "board": [
            {
                "board_id": 1,
                "title": "Software Developer",
                "owner": "Homer J Simpson",
                "cards": []
            }
        ]
    }
    

def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Board id 1 is not found"
    }

def test_create_board1(client):
    # Act
    response = client.post("/boards", json={"title": "New Board", "owner": "New Owner"})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body["board"]["title"] == "New Board"
    assert response_body["board"]["owner"] == "New Owner"

def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Tests always work!",
        "owner": "Sonic",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "board": {
            "board_id": 1,
            "cards": [],
            "owner": "Sonic",
            "title": "Tests always work!"
    }
}
    new_board = Board.query.get(1)
    new_board = db.session.get(Board, 1)
    assert new_board
    assert new_board.title == "Tests always work!"
    assert new_board.owner == "Sonic"