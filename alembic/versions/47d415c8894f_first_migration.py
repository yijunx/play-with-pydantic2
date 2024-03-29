"""first migration

Revision ID: 47d415c8894f
Revises: 
Create Date: 2024-01-30 09:27:00.024812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47d415c8894f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors_table',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('nationality', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books_table',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('isbn', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author_book_relations_table',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('book_id', sa.String(), nullable=False),
    sa.Column('author_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors_table.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chapters_table',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('starting_page', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chapters_table')
    op.drop_table('author_book_relations_table')
    op.drop_table('books_table')
    op.drop_table('authors_table')
    # ### end Alembic commands ###
