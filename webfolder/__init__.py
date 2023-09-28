"""This is the __init__ file that creates the website application
along with the database needed for the username, email ,and password"""
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """This creates the Flask website. It initiates the
    log in manager that would manage the users and
    initiates the url prefix for view and authenticate."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wqdqdqwdqwfr2r12e12wasdawd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'authenticate.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(identification):
        return User.query.get(int(identification))

    from webfolder.view import views
    from webfolder.authenticate import authenticate

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authenticate, url_prefix='/')

    from webfolder.model import User, PasswordReset
    create_database(app)
    return app


def create_database(app):
    """This function creates the database needed
    to store the email, password, and username."""
    if not path.exists('webfolder/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')
