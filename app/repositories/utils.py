from app.models.pagination import ResponsePagination, QueryPagination


def translate_query_pagination(
    query_pagination: QueryPagination, total: int
) -> tuple[int, int, ResponsePagination]:
    """
    returns limit: int and offset: int and paging: ResponsePagination
    with pagesize undesided
    """
    limit = query_pagination.size or total
    offset = (query_pagination.page - 1) * limit if query_pagination.page else 0
    current_page = query_pagination.page or 1

    # well here the default paghe size is set...
    # i guess we shall remove it first..
    total_pages = -(-total // query_pagination.size) if query_pagination.size else 1

    paging = ResponsePagination(
        total=total,
        total_pages=total_pages,
        current_page=current_page,
        page_size=max(0, min((total - offset), limit)),
    )
    return limit, offset, paging
