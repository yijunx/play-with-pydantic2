from flask import Blueprint
from flask_pydantic import validate


bp = Blueprint("book", __name__, url_prefix="/apis/online-library/books")


@bp.route("", methods=["GET"])
def get_books(): ...
