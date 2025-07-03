from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .routes import main
    from .auth import auth as auth_blueprint
    from .admin import admin as admin_blueprint

    # ✅ Register each blueprint ONCE
    app.register_blueprint(main)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # Moved import here to avoid circular import
    from .models import Admin

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    return app
