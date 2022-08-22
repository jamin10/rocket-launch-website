from . import db 
from flask_login import UserMixin


# Set up launch model
class Launch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # Reference other table, 1 to many relationship 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# Set up user model 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    launches = db.relationship('Launch')


