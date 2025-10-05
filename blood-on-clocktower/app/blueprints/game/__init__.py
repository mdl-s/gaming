"""Blueprint pour la gestion des parties."""
from flask import Blueprint

bp = Blueprint('game', __name__)

from app.blueprints.game import routes

