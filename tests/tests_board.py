from app.models.board import Board
from app.db import db
import pytest

def test_get_board_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_boards_one_saved_boards(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title":"Software Developer", 
            "owner":"Homer J Simpson"
        }
    ]

def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message":"board id 1 is not found"
    }

def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Tests always work!",
        "owner":"Sonic",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "id": 1,
        "title": "Tests always work!",
        "owner":"Sonic",
    }
    # new_board = Board.query.get(1)
    new_board = db.session.get(Board, 1)
    assert new_board
    assert new_board.title == "Tests always work!"
    assert new_board.owner == "Sonic"

def test_update_board(client, one_board):
    # Act
    response = client.put("/boards/1", json={
            "title": "Updated Board!",
            "owner":"Updated Owner",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "id": 1,
        "title": "Updated Board!",
        "owner":"Updated Owner",
    }
    updated_board = db.session.get(Board, 1)
    assert updated_board.title == "Updated Board!"
    assert updated_board.owner == "Updated Owner"

def test_update_board_not_found(client, one_board):
    # Act
    response = client.put("/boards/1", json={
            "title": "Updated Board!",
            "owner":"Updated Owner",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message":"Task id 1 is not found"
    }

def test_delete_all_boards(client, one_task_belongs_to_one_goal, three_tasks):
    # Act
    response = client.delete("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "details": f'All Boards and Cards are successfully deleted'
    }
    assert len(db.session.get(Board, 1).cards) == 0
