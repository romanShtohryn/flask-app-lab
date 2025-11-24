from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # реєстрація блюпринтів
    from app.posts import post_bp
    app.register_blueprint(post_bp, url_prefix="/post")

    from app.users import users_bp
    app.register_blueprint(users_bp, url_prefix="/users")

    from app.products import products_bp
    app.register_blueprint(products_bp, url_prefix="/products")

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
