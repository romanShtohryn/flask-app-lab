from flask import render_template
from . import products_bp

@products_bp.route("/")
def list_products():
    products = [
        {"id": 1, "name": "Flask Course", "price": "Free"},
        {"id": 2, "name": "Python Book", "price": "€20"},
    ]
    return render_template("products/list.html", products=products)
