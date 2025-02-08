

from flask import Flask
# from models import db, User
from flask_login import LoginManager
# from views import main_blueprint
# from auth import auth_blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # check if testing app, to configure the app for testing
    if os.environ.get('CONFIG_TYPE') == 'config.TestingConfig':
        app.config['SECRET_KEY'] = 'secret'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    else:
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("postgres", "postgresql", 1)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'

    from .models import User
    from .views import main_blueprint
    # from .auth import auth_blueprint

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Register blueprint for routes
    app.register_blueprint(main_blueprint)
    # app.register_blueprint(auth_blueprint)

    #if __name__ == '__main__':
    with app.app_context():
        print('Creating tables')
        db.create_all()  # Create tables (if not created)
        #app.run(debug=True)

    return app


if __name__ == '__main__':
    create_app()