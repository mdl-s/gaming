"""Blueprint pour l'interface Grimoire (tableau du Conteur)."""
from flask import Blueprint

bp = Blueprint('grimoire', __name__)

from app.blueprints.grimoire import routes

