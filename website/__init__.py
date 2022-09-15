from os import path
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialise database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'foobafoo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Tell flask where to store database and to use it for the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Launch

    # Tell login manager where to go if not logged in 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Tell flask how to load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    create_database(app)

    return app

# Create the database if doesn't already exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')