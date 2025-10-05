"""Routes pour l'administration."""
from flask import render_template, redirect, url_for, flash, request
from app.blueprints.admin import bp
from app.models import db, Edition, Character


@bp.route('/')
def index():
    """Page d'administration."""
    editions = Edition.query.all()
    characters = Character.query.count()
    
    return render_template('admin/index.html',
                         editions=editions,
                         characters_count=characters)


@bp.route('/characters')
def characters():
    """Liste des personnages."""
    edition_id = request.args.get('edition_id', type=int)
    
    query = Character.query
    if edition_id:
        query = query.filter_by(edition_id=edition_id)
    
    characters = query.order_by(Character.character_type, Character.name).all()
    editions = Edition.query.all()
    
    return render_template('admin/characters.html',
                         characters=characters,
                         editions=editions,
                         selected_edition=edition_id)


@bp.route('/editions')
def editions():
    """Liste des éditions."""
    editions = Edition.query.all()
    return render_template('admin/editions.html', editions=editions)


@bp.route('/scripts')
def scripts():
    """Liste des scripts personnalisés."""
    # TODO: Implémenter le modèle Script
    scripts = []  # Script.query.all()
    
    editions = Edition.query.filter_by(is_active=True).all()
    characters = Character.query.all()
    
    return render_template('admin/scripts.html', 
                         scripts=scripts,
                         editions=editions,
                         characters=characters)


@bp.route('/scripts/create', methods=['POST'])
def create_script():
    """Créer un nouveau script personnalisé."""
    # TODO: Implémenter la création de script
    flash('Fonctionnalité de scripts personnalisés à venir !', 'info')
    return redirect(url_for('admin.scripts'))

