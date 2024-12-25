from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Card(db.Model):
    card_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey('board.board_id'))
    board: Mapped['Board'] = relationship('Board', back_populates='cards')

    def to_dict(self):
        return {
            'card_id': self.card_id,
            'message': self.message,
            'likes_count': self.likes_count,
            'board_id': self.board_id
        }

    @classmethod
    def from_dict(cls, data):
        return Card(message=data['message'], likes_count=data['likes_count'], board_id=data['board_id'])