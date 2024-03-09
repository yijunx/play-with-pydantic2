from pydantic import BaseModel
from typing import Optional


class QueryPagination(BaseModel):
    page: int = 1
    size: int = 5


class ResponsePagination(BaseModel):
    total: int
    page_size: int
    current_page: int
    total_pages: int
