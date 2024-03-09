from sqlalchemy.orm import Session
from app.repositories.base import Repository
from app.models.sqlalchemy import BookORM


class AuthorRepository(Repository[BookORM]):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__()
