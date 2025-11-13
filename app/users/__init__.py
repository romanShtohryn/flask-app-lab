from flask import Blueprint

users_bp = Blueprint(
    "users",
    __name__,
    template_folder="templates"
)

# Import routes so they attach to users_bp
from . import views
