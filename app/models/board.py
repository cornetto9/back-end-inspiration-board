from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING

class Board(db.Model):
    board_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    owner: Mapped[str]
    cards: Mapped[list['Card']] = relationship('Card', back_populates='board')

    def to_dict(self):
        return {
            'board_id': self.board_id,
            'title': self.title,
            'owner': self.owner,
            'cards': [card.to_dict() for card in self.cards]
        }
    @classmethod
    def from_dict(cls, data):
        return Board(title=data['title'], owner=data['owner'])
    
