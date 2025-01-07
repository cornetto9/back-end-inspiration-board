from app.models.board import Board
from app.db import db

def test_get_all_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == {"board": []}

def test_get_boards_one_saved_boards(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {
        "board": 
            {
                "board_id": 1,
                "title": "Software Developer",
                "owner": "Homer J Simpson",
                "cards": []
            }
    }

def test_get_all_boards_one_saved_board(client, one_board):
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

def test_create_board_missing_owner_returns_invalid_data(client):
    # Act
    response = client.post("/boards", json={"title": "New Board"})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }

def test_create_board_missing_title_returns__invalid_data(client):
    # Act
    response = client.post("/boards", json={"owner": "Sonic"})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }

def test_create_board_stdout(client):
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
    new_board = db.session.get(Board, 1)
    new_board = db.session.get(Board, 1)
    assert new_board
    assert new_board.title == "Tests always work!"
    assert new_board.owner == "Sonic"

def test_delete_one_board(client, one_board):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Board 1 and its cards have been deleted"}

def test_delete_board_with_cards(client, one_board_with_cards):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Board 1 and its cards have been deleted"}