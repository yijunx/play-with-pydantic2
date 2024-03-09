from abc import ABC, abstractclassmethod
from app.models.pagination import ResponsePagination, QueryPagination


# well not sure if this is any useful??
class Repository[T](ABC):
    @abstractclassmethod
    def get_one(self, id: str) -> T:
        raise NotImplementedError

    @abstractclassmethod
    def get_all(
        self, query_pagination: QueryPagination
    ) -> tuple[list[T], ResponsePagination]:
        raise NotImplementedError

    @abstractclassmethod
    def create(self, payload: object) -> T:
        raise NotImplementedError

    @abstractclassmethod
    def patch(self, id: str, payload: object) -> T:
        raise NotImplementedError

    @abstractclassmethod
    def delete_one(self, id: str) -> None:
        raise NotImplementedError
