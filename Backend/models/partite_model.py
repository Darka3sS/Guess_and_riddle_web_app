from extentions import db
from sqlalchemy.dialects.postgresql import TIMESTAMP


class partite(db.Model):
    __tablename__ = "partite"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(TIMESTAMP(timezone=True), nullable=False)
    score_correct_games = db.Column(db.Integer, default=0)
    score_games_played = db.Column(db.Integer, default=0)

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date.isoformat() if self.date else None,
            "score_correct_games": self.score_correct_games,
            "score_games_played": self.score_games_played,
        }
