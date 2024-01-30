from sqlalchemy.orm import Session
from app.repositories.base import Repository
from app.models.sqlalchemy import AuthorORM
from app.models.pagination import ResponsePagination



class AuthorRepository(Repository[AuthorORM]):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__()

    def get_one(self, id: str) -> AuthorORM:

        raise NotImplementedError
    

    def get_all(self, id: str) -> tuple[list[AuthorORM], ResponsePagination]:
        raise NotImplementedError
    

    def create(self, payload: object) -> AuthorORM:
        raise NotImplementedError
    

    def patch(self, id: int, payload: object) -> AuthorORM:
        raise NotImplementedError
    

    def delete_one(self, id: int) -> None:
        raise NotImplementedError