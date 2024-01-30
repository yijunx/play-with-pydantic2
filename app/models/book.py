from pydantic import BaseModel


class Author(BaseModel):
    name: str
    nationality: str


class Chapter(BaseModel):
    name: str
    starting_page: int


class Book(BaseModel):
    author: Author
    chapters: list[Chapter]
    isbn: str


if __name__ == "__main__":
    author = Author(name="tom", nationality="Swiss")
    book = Book(
        author=author,
        chapters=[Chapter(name="chapter1", starting_page=1)],
        isbn="isbn-00003-49951"
    )
    # just print
    print(book)

    # to get string
    print(book.model_dump_json())

    # to get dict
    print(book.model_dump())