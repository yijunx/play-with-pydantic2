from flask import Flask
from app.apis.author import bp as author_bp
from app.apis.book import bp as book_bp


app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp)
    app.register_blueprint(author_bp)
    return app
