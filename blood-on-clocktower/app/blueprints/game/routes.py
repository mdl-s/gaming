"""Routes pour la gestion des parties."""
from flask import render_template, redirect, url_for, flash, request, jsonify
from app.blueprints.game import bp
from app.models import db, Game, Edition, Character, Player
from datetime import datetime
import random


# Distribution des rôles selon le nombre de joueurs
PLAYER_DISTRIBUTION = {
    5: {'townsfolk': 3, 'outsider': 0, 'minion': 1, 'demon': 1},
    6: {'townsfolk': 3, 'outsider': 1, 'minion': 1, 'demon': 1},
    7: {'townsfolk': 5, 'outsider': 0, 'minion': 1, 'demon': 1},
    8: {'townsfolk': 5, 'outsider': 1, 'minion': 1, 'demon': 1},
    9: {'townsfolk': 5, 'outsider': 2, 'minion': 1, 'demon': 1},
    10: {'townsfolk': 7, 'outsider': 0, 'minion': 2, 'demon': 1},
    11: {'townsfolk': 7, 'outsider': 1, 'minion': 2, 'demon': 1},
    12: {'townsfolk': 7, 'outsider': 2, 'minion': 2, 'demon': 1},
    13: {'townsfolk': 9, 'outsider': 0, 'minion': 3, 'demon': 1},
    14: {'townsfolk': 9, 'outsider': 1, 'minion': 3, 'demon': 1},
    15: {'townsfolk': 9, 'outsider': 2, 'minion': 3, 'demon': 1},
}


@bp.route('/new', methods=['GET', 'POST'])
def new_game():
    """Créer une nouvelle partie."""
    if request.method == 'POST':
        game_name = request.form.get('game_name')
        edition_id = request.form.get('edition_id', type=int)
        player_count = request.form.get('player_count', type=int)
        
        # Validation
        if not game_name:
            flash('Le nom de la partie est requis.', 'error')
            return redirect(url_for('game.new_game'))
        
        if not edition_id:
            flash("Veuillez sélectionner une édition.", 'error')
            return redirect(url_for('game.new_game'))
        
        if player_count not in PLAYER_DISTRIBUTION:
            flash(f'Le nombre de joueurs doit être entre 5 et 15.', 'error')
            return redirect(url_for('game.new_game'))
        
        # Créer la partie
        game = Game(
            name=game_name,
            edition_id=edition_id,
            player_count=player_count,
            status=Game.SETUP
        )
        db.session.add(game)
        db.session.commit()
        
        flash(f'Partie "{game_name}" créée avec succès !', 'success')
        return redirect(url_for('game.setup', game_id=game.id))
    
    # GET
    editions = Edition.query.filter_by(is_active=True).all()
    return render_template('game/new.html', editions=editions)


@bp.route('/<int:game_id>/setup', methods=['GET', 'POST'])
def setup(game_id):
    """Configuration de la partie (ajout des joueurs)."""
    game = Game.query.get_or_404(game_id)
    
    if game.status != Game.SETUP:
        flash('Cette partie a déjà été configurée.', 'warning')
        return redirect(url_for('grimoire.view', game_id=game.id))
    
    if request.method == 'POST':
        # Récupérer les noms des joueurs
        player_names = []
        for i in range(1, game.player_count + 1):
            name = request.form.get(f'player_{i}')
            if name:
                player_names.append(name.strip())
        
        if len(player_names) != game.player_count:
            flash(f'Veuillez entrer les noms de tous les {game.player_count} joueurs.', 'error')
            return redirect(url_for('game.setup', game_id=game.id))
        
        # Distribuer les rôles
        try:
            distribute_roles(game, player_names)
            db.session.commit()
            flash('Rôles distribués avec succès !', 'success')
            return redirect(url_for('game.view', game_id=game.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Erreur lors de la distribution des rôles : {str(e)}', 'error')
            return redirect(url_for('game.setup', game_id=game.id))
    
    # GET
    distribution = PLAYER_DISTRIBUTION[game.player_count]
    return render_template('game/setup.html', game=game, distribution=distribution)


def distribute_roles(game: Game, player_names: list):
    """
    Distribue aléatoirement les rôles aux joueurs.
    
    Args:
        game: La partie en cours
        player_names: Liste des noms des joueurs
    """
    distribution = PLAYER_DISTRIBUTION[game.player_count]
    
    # Récupérer les personnages disponibles pour cette édition
    edition_characters = {
        'townsfolk': Character.query.filter_by(
            edition_id=game.edition_id,
            character_type=Character.TOWNSFOLK
        ).all(),
        'outsider': Character.query.filter_by(
            edition_id=game.edition_id,
            character_type=Character.OUTSIDER
        ).all(),
        'minion': Character.query.filter_by(
            edition_id=game.edition_id,
            character_type=Character.MINION
        ).all(),
        'demon': Character.query.filter_by(
            edition_id=game.edition_id,
            character_type=Character.DEMON
        ).all(),
    }
    
    # Vérifier qu'il y a assez de personnages
    for char_type, count in distribution.items():
        if len(edition_characters[char_type]) < count:
            raise ValueError(f"Pas assez de personnages de type {char_type} dans cette édition.")
    
    # Sélectionner aléatoirement les personnages
    selected_characters = []
    
    for char_type, count in distribution.items():
        selected = random.sample(edition_characters[char_type], count)
        selected_characters.extend(selected)
    
    # Mélanger les personnages et les assigner aux joueurs
    random.shuffle(selected_characters)
    
    # Créer les joueurs
    for position, (name, character) in enumerate(zip(player_names, selected_characters), start=1):
        player = Player(
            game_id=game.id,
            name=name,
            seat_position=position,
            character_id=character.id,
            alignment=character.alignment,
            is_alive=True
        )
        
        # Gérer le Drunk (il croit être un Townsfolk)
        if character.name == 'Drunk':
            # Le Drunk est techniquement bon même s'il ne marche pas
            player.is_drunk = True
        
        db.session.add(player)


@bp.route('/<int:game_id>')
def view(game_id):
    """Voir les détails d'une partie."""
    game = Game.query.get_or_404(game_id)
    return render_template('game/view.html', game=game)


@bp.route('/<int:game_id>/start', methods=['POST'])
def start_game(game_id):
    """Démarrer la partie (passer de setup à in_progress)."""
    game = Game.query.get_or_404(game_id)
    
    if game.status != Game.SETUP:
        flash('Cette partie ne peut pas être démarrée.', 'error')
        return redirect(url_for('game.view', game_id=game.id))
    
    game.start_game()
    db.session.commit()
    
    flash('La partie a commencé ! Première nuit...', 'success')
    return redirect(url_for('grimoire.view', game_id=game.id))


@bp.route('/<int:game_id>/delete', methods=['POST'])
def delete_game(game_id):
    """Supprimer une partie."""
    game = Game.query.get_or_404(game_id)
    
    db.session.delete(game)
    db.session.commit()
    
    flash(f'Partie "{game.name}" supprimée.', 'success')
    return redirect(url_for('main.index'))


@bp.route('/list')
def list_games():
    """Liste toutes les parties."""
    games = Game.query.order_by(Game.created_at.desc()).all()
    return render_template('game/list.html', games=games)

