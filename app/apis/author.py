from flask import Blueprint


bp = Blueprint("author", __name__, url_prefix="/apis/online-library/authors")


@bp.route("", methods=["GET"])
def get_authors(): ...
