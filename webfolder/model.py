"""This part of the code creates the model of the
contents of the  website database"""
from flask_login import UserMixin
from sqlalchemy.sql import func
from webfolder import db


# pylint: disable=too-few-public-methods
class Blog(db.Model):
    """This class creates the parameters of the database for Blog"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# pylint: disable=too-few-public-methods
class User(db.Model, UserMixin):
    """This class creates the parameters of a user account"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    username = db.Column(db.String(120))
    blogs = db.relationship('Blog')
    reset = db.relationship('PasswordReset')

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


# pylint: disable=too-few-public-methods
class PasswordReset(db.Model):
    """This class creates the parameter for the password reset"""
    id = db.Column(db.Integer, primary_key=True)
    reset_key = db.Column(db.String(120), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetime = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.relationship(User, lazy='joined')
    has_activated = db.Column(db.Boolean, default=False)

    def __init__(self, reset_key, user_id, datetime1, has_activated):
        self.reset_key = reset_key
        self.user_id = user_id
        self.datetime = datetime1
        self.has_activated = has_activated
