from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes

def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
