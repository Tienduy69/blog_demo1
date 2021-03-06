from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_database(app):
    #if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:261297@localhost/bai1"
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .models import User, Note
    create_database(app)

    from .views import views
    from .user import user

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(user, url_prefix='/')





    login_manager = LoginManager()
    login_manager.login_view = 'user.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


