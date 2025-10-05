"""Routes principales de l'application."""
from flask import render_template, redirect, url_for
from app.blueprints.main import bp
from app.models import db, Game, Edition


@bp.route('/')
def index():
    """Page d'accueil."""
    recent_games = Game.query.order_by(Game.created_at.desc()).limit(5).all()
    editions = Edition.query.filter_by(is_active=True).all()
    
    return render_template('main/index.html', 
                         recent_games=recent_games,
                         editions=editions)


@bp.route('/rules')
def rules():
    """Page des règles du jeu."""
    return render_template('main/rules.html')


@bp.route('/about')
def about():
    """Page à propos."""
    return render_template('main/about.html')

