from flask import Blueprint


bp = Blueprint("book", __name__, url_prefix="/apis/online-library/books")


@bp.route("", methods=["GET"])
def get_books(): ...
