from reader import app, db
from sqlalchemy.sql import func


class Book(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    ganre = db.Column(db.String(20), nullable=False)
    ratting = db.Column(db.INTEGER)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    description = db.Column(db.TEXT)
    notes = db.Column(db.TEXT)
    createde_at = db.Column(db.DATETIME(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Book {self.title}>'
