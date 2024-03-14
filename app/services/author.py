from app.repositories.author import AuthorRepository
from app.utils.db import get_db
from app.models.models import AuthorCreate, Author

def add_author(payload: AuthorCreate):
    with get_db() as db:
        repo = AuthorRepository(db=db)
        db_item = repo.create(payload=payload)
        item = Author.model_validate(db_item)
    return item