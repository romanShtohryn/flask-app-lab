from flask import Flask

app = Flask(__name__)

# базові маршрути
from . import views

# імпорт та реєстрація users blueprint
from .users import users_bp
app.register_blueprint(users_bp, url_prefix="/users")

# імпорт та реєстрація products blueprint (пізніше)
# from .products import products_bp
# app.register_blueprint(products_bp, url_prefix="/products")
