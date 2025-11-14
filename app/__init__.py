from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("../config.py")

from . import views

from .users import users_bp
app.register_blueprint(users_bp, url_prefix="/users")

from .products import products_bp
app.register_blueprint(products_bp, url_prefix="/products")

@app.context_processor
def inject_theme():
    from flask import request
    theme = request.cookies.get("theme", "light")
    return dict(theme=theme)
