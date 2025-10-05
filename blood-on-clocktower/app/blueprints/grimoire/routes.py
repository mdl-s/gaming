"""Routes pour l'interface Grimoire."""
from flask import render_template, redirect, url_for, flash, request, jsonify
from app.blueprints.grimoire import bp
from app.models import db, Game, Player, NightAction, DayAction, ReminderToken, Character
from datetime import datetime
from sqlalchemy import or_


@bp.route('/<int:game_id>')
def view(game_id):
    """Afficher le Grimoire pour une partie."""
    game = Game.query.get_or_404(game_id)
    
    if game.status == Game.SETUP:
        flash('La partie n\'a pas encore été démarrée.', 'warning')
        return redirect(url_for('game.setup', game_id=game.id))
    
    # Récupérer les joueurs ordonnés par position
    players = game.players.order_by(Player.seat_position).all()
    
    # Récupérer les personnages pour l'ordre de nuit
    characters_in_game = [p.character for p in players]
    
    # Ordre de nuit
    if game.current_night_number == 1:
        night_order = sorted(
            [c for c in characters_in_game if c.first_night],
            key=lambda c: c.first_night
        )
    else:
        night_order = sorted(
            [c for c in characters_in_game if c.other_nights],
            key=lambda c: c.other_nights
        )
    
    return render_template('grimoire/view.html', 
                         game=game, 
                         players=players,
                         night_order=night_order)


@bp.route('/<int:game_id>/player/<int:player_id>')
def player_detail(game_id, player_id):
    """Détails d'un joueur spécifique."""
    game = Game.query.get_or_404(game_id)
    player = Player.query.get_or_404(player_id)
    
    if player.game_id != game.id:
        flash('Ce joueur n\'appartient pas à cette partie.', 'error')
        return redirect(url_for('grimoire.view', game_id=game.id))
    
    # Récupérer l'historique des actions
    night_actions = player.night_actions_made.order_by(NightAction.timestamp.desc()).all()
    
    return render_template('grimoire/player_detail.html',
                         game=game,
                         player=player,
                         night_actions=night_actions)


@bp.route('/<int:game_id>/next-phase', methods=['POST'])
def next_phase(game_id):
    """Passer à la phase suivante (jour -> nuit ou nuit -> jour)."""
    game = Game.query.get_or_404(game_id)
    
    if game.status != Game.IN_PROGRESS:
        flash('La partie n\'est pas en cours.', 'error')
        return redirect(url_for('grimoire.view', game_id=game.id))
    
    game.next_phase()
    db.session.commit()
    
    if game.current_phase == Game.DAY:
        flash(f'Jour {game.current_day_number} commencé !', 'success')
    else:
        flash(f'Nuit {game.current_night_number} commencée !', 'success')
    
    return redirect(url_for('grimoire.view', game_id=game.id))


@bp.route('/<int:game_id>/player/<int:player_id>/kill', methods=['POST'])
def kill_player(game_id, player_id):
    """Tuer un joueur."""
    game = Game.query.get_or_404(game_id)
    player = Player.query.get_or_404(player_id)
    
    if player.game_id != game.id:
        return jsonify({'error': 'Invalid player'}), 400
    
    if not player.is_alive:
        return jsonify({'error': 'Player already dead'}), 400
    
    # Tuer le joueur
    if game.current_phase == Game.NIGHT:
        player.kill(night_number=game.current_night_number)
    else:
        player.kill(day_number=game.current_day_number)
    
    db.session.commit()
    
    return jsonify({'success': True, 'player': player.name})


@bp.route('/<int:game_id>/player/<int:player_id>/revive', methods=['POST'])
def revive_player(game_id, player_id):
    """Ressusciter un joueur (pour corriger une erreur)."""
    game = Game.query.get_or_404(game_id)
    player = Player.query.get_or_404(player_id)
    
    if player.game_id != game.id:
        return jsonify({'error': 'Invalid player'}), 400
    
    player.is_alive = True
    player.death_night = None
    player.death_day = None
    player.used_dead_vote = False
    
    db.session.commit()
    
    return jsonify({'success': True, 'player': player.name})


@bp.route('/<int:game_id>/player/<int:player_id>/toggle-poison', methods=['POST'])
def toggle_poison(game_id, player_id):
    """Basculer l'état empoisonné d'un joueur."""
    game = Game.query.get_or_404(game_id)
    player = Player.query.get_or_404(player_id)
    
    if player.game_id != game.id:
        return jsonify({'error': 'Invalid player'}), 400
    
    player.is_poisoned = not player.is_poisoned
    db.session.commit()
    
    return jsonify({'success': True, 'is_poisoned': player.is_poisoned})


@bp.route('/<int:game_id>/player/<int:player_id>/notes', methods=['POST'])
def update_notes(game_id, player_id):
    """Mettre à jour les notes d'un joueur."""
    game = Game.query.get_or_404(game_id)
    player = Player.query.get_or_404(player_id)
    
    if player.game_id != game.id:
        return jsonify({'error': 'Invalid player'}), 400
    
    notes = request.json.get('notes', '')
    player.notes = notes
    db.session.commit()
    
    return jsonify({'success': True})


@bp.route('/<int:game_id>/end', methods=['POST'])
def end_game(game_id):
    """Terminer la partie."""
    game = Game.query.get_or_404(game_id)
    
    winner = request.form.get('winner')  # 'good' ou 'evil'
    
    if winner not in [Game.GOOD, Game.EVIL]:
        flash('Gagnant invalide.', 'error')
        return redirect(url_for('grimoire.view', game_id=game.id))
    
    game.end_game(winner)
    db.session.commit()
    
    winner_name = 'Bien' if winner == Game.GOOD else 'Mal'
    flash(f'Partie terminée ! Le {winner_name} a gagné !', 'success')
    
    return redirect(url_for('game.view', game_id=game.id))


@bp.route('/<int:game_id>/nomination', methods=['POST'])
def add_nomination(game_id):
    """Ajouter une nomination."""
    game = Game.query.get_or_404(game_id)
    
    nominator_id = request.form.get('nominator_id', type=int)
    nominee_id = request.form.get('nominee_id', type=int)
    
    if not nominator_id or not nominee_id:
        flash('Nominateur et nominé requis.', 'error')
        return redirect(url_for('grimoire.view', game_id=game.id))
    
    nomination = DayAction(
        game_id=game.id,
        day_number=game.current_day_number,
        action_type=DayAction.NOMINATION,
        nominator_id=nominator_id,
        nominee_id=nominee_id
    )
    
    db.session.add(nomination)
    db.session.commit()
    
    flash('Nomination enregistrée.', 'success')
    return redirect(url_for('grimoire.view', game_id=game.id))


@bp.route('/<int:game_id>/vote/<int:nomination_id>', methods=['POST'])
def record_vote(game_id, nomination_id):
    """Enregistrer le résultat d'un vote."""
    game = Game.query.get_or_404(game_id)
    nomination = DayAction.query.get_or_404(nomination_id)
    
    if nomination.game_id != game.id:
        return jsonify({'error': 'Invalid nomination'}), 400
    
    vote_count = request.json.get('vote_count', 0)
    votes_against = request.json.get('votes_against', 0)
    executed = request.json.get('executed', False)
    notes = request.json.get('notes', '')
    
    nomination.vote_count = vote_count
    nomination.votes_against = votes_against
    nomination.executed = executed
    nomination.notes = notes
    
    # Si exécution, tuer le joueur
    if executed:
        nominee = Player.query.get(nomination.nominee_id)
        nominee.kill(day_number=game.current_day_number)
    
    db.session.commit()
    
    return jsonify({'success': True})


@bp.route('/<int:game_id>/history')
def history(game_id):
    """Afficher l'historique complet de la partie."""
    game = Game.query.get_or_404(game_id)
    
    return render_template('grimoire/history.html', game=game, db=db)


@bp.route('/<int:game_id>/night-action', methods=['POST'])
def add_night_action(game_id):
    """Enregistrer une action de nuit."""
    game = Game.query.get_or_404(game_id)
    
    if game.current_phase != Game.NIGHT:
        return jsonify({'error': 'Pas en phase de nuit'}), 400
    
    player_id = request.json.get('player_id')
    action_type = request.json.get('action_type')
    target_player_id = request.json.get('target_player_id')
    result = request.json.get('result')
    notes = request.json.get('notes', '')
    
    player = Player.query.get_or_404(player_id)
    
    night_action = NightAction(
        game_id=game.id,
        night_number=game.current_night_number,
        character_id=player.character_id,
        player_id=player_id,
        action_type=action_type,
        target_player_id=target_player_id,
        result=result,
        notes=notes
    )
    
    db.session.add(night_action)
    db.session.commit()
    
    return jsonify({'success': True, 'action_id': night_action.id})

