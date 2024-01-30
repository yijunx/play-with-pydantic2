from pydantic import BaseModel
from typing import Optional


class QueryPagination(BaseModel):
    page: Optional[int] = 1
    size: Optional[int] = 5


class ResponsePagination(BaseModel):
    total: int
    page_size: int
    current_page: int
    total_pages: int
