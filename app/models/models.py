from pydantic import BaseModel


class AuthorCreate(BaseModel):
    name: str
    nationality: str


class Author(AuthorCreate):
    id: str


class ChapterCreate(BaseModel):
    name: str
    starting_page: int


class Chapter(ChapterCreate):
    id: str


class BookCreate(BaseModel):
    title: str
    isbn: str
    author_ids: list[str]


class Book(BookCreate):
    id: str

    # relation
    authors: list[Author]
    chapters: list[Chapter]


if __name__ == "__main__":
    author = Author(id="qwe", name="tom", nationality="Swiss")
    book = Book(
        authors=[author],
        chapters=[Chapter(name="chapter1", starting_page=1)],
        isbn="isbn-00003-49951",
    )
    # just print
    print(book)

    # to get string
    print(book.model_dump_json())

    # to get dict
    print(book.model_dump())
