from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True

    return app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


from app import routes, models, forms
db.create_all()
