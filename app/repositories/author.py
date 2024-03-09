from sqlalchemy.orm import Session
from app.repositories.base import Repository
from app.models.sqlalchemy import AuthorORM
from app.models.pagination import ResponsePagination, QueryPagination
from app.models.exceptions import CustomError
from app.models.models import AuthorCreate
from app.repositories.utils import translate_query_pagination
from uuid import uuid4
from datetime import datetime, timezone


class AuthorRepository(Repository[AuthorORM]):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__()

    def get_one(self, id: str) -> AuthorORM:
        db_item = self.db.query(AuthorORM).filter(AuthorORM.id == id).first()

        if db_item:
            return db_item
        else:
            raise CustomError(status_code=404, message="author not found")

    def get_all(
        self, query_pagination: QueryPagination
    ) -> tuple[list[AuthorORM], ResponsePagination]:
        query = self.db.query(AuthorORM).filter(AuthorORM.id == id)

        total = query.count()

        limit, offset, p = translate_query_pagination(
            query_pagination=query_pagination, total=total
        )

        db_items = query.offset(offset).limit(limit)

        return db_items, p

    def create(self, payload: AuthorCreate) -> AuthorORM:
        db_item = AuthorORM(
            id=str(uuid4()),
            name=payload.name,
            nationality=payload.nationality,
            created_at=datetime.now(timezone.utc)
        )
        self.db.add(db_item)
        self.db.flush()
        return db_item

    def patch(self, id: int, payload: object) -> AuthorORM:
        db_item = self.get_one(
            id=id
        )
        # modify the db_item here

    def delete_one(self, id: int) -> None:
        db_item = self.get_one(
            id=id
        )
        self.db.delete(db_item)
        
