from datetime import datetime

from sqlalchemy import (
    Integer,
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.sqlalchemy.base import Base


class AuthorORM(Base):
    __tablename__ = "authors_table"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    nationality: Mapped[str] = mapped_column(String, nullable=False)

    # admin fields
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # property
    books: Mapped[list["BookORM"]] = relationship(
        secondary="author_book_relations_table", back_populates="authors"
    )


class BookORM(Base):
    __tablename__ = "books_table"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    isbn: Mapped[str] = mapped_column(String, nullable=False)

    # admin fields
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # properties
    chapters: Mapped["ChapterORM"] = relationship(back_populates="book")

    # property
    authors: Mapped[list["BookORM"]] = relationship(
        secondary="author_book_relations_table", back_populates="authors"
    )


class AuthorBookRelationORM(Base):
    __tablename__ = "author_book_relations_table"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    book_id: Mapped[str] = mapped_column(ForeignKey("books_table.id"), nullable=False)
    author_id: Mapped[str] = mapped_column(
        ForeignKey("authors_table.id"), nullable=False
    )

    # admin fields
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class ChapterORM(Base):
    __tablename__ = "chapters_table"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    starting_page: Mapped[int] = mapped_column(Integer, nullable=False)

    # for relation
    book_id: Mapped[str] = mapped_column(ForeignKey("books_table.id"), nullable=False)
    # properties
    book: Mapped["BookORM"] = relationship(back_populates="chapters")
