from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sae.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from sae.main.routes import main
        from sae.users.routes import users
        from sae.characters.routes import characters
        app.register_blueprint(users)
        app.register_blueprint(main)
        app.register_blueprint(characters)

        return app

    return app