from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Board(db.Model):
    board_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    owner: Mapped[str]

    def to_dict(self):
        return {
            'board_id': self.board_id,
            'title': self.title,
            'owner': self.owner
        }

