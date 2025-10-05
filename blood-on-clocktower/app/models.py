"""Modèles de données pour Blood on the Clocktower."""
from datetime import datetime
from typing import Optional
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Edition(db.Model):
    """Éditions du jeu (Trouble Brewing, Bad Moon Rising, etc.)."""
    
    __tablename__ = 'editions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    difficulty_level = db.Column(db.Integer, default=1)  # 1=Débutant, 2=Intermédiaire, 3=Avancé
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    characters = db.relationship('Character', back_populates='edition', lazy='dynamic')
    games = db.relationship('Game', back_populates='edition', lazy='dynamic')
    
    def __repr__(self):
        return f'<Edition {self.name}>'


class Character(db.Model):
    """Personnages du jeu."""
    
    __tablename__ = 'characters'
    
    # Types de personnages
    TOWNSFOLK = 'townsfolk'
    OUTSIDER = 'outsider'
    MINION = 'minion'
    DEMON = 'demon'
    TRAVELLER = 'traveller'
    
    CHARACTER_TYPES = [TOWNSFOLK, OUTSIDER, MINION, DEMON, TRAVELLER]
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    edition_id = db.Column(db.Integer, db.ForeignKey('editions.id'), nullable=False)
    character_type = db.Column(db.String(20), nullable=False)
    
    # Informations sur le personnage
    ability_description = db.Column(db.Text, nullable=False)
    first_night = db.Column(db.Integer)  # Ordre d'activation première nuit (null si pas actif)
    other_nights = db.Column(db.Integer)  # Ordre d'activation autres nuits
    setup_info = db.Column(db.Text)  # Informations spéciales de setup
    
    # Tokens de rappel (format JSON: ["token1", "token2"])
    remind_tokens = db.Column(db.JSON)
    
    # Image
    image_url = db.Column(db.String(255))
    
    # Métadonnées
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    edition = db.relationship('Edition', back_populates='characters')
    players = db.relationship('Player', back_populates='character', lazy='dynamic')
    
    def __repr__(self):
        return f'<Character {self.name} ({self.character_type})>'
    
    @property
    def alignment(self):
        """Retourne l'alignement du personnage."""
        if self.character_type in [self.TOWNSFOLK, self.OUTSIDER]:
            return 'good'
        elif self.character_type in [self.MINION, self.DEMON]:
            return 'evil'
        return 'neutral'


class Game(db.Model):
    """Parties de Blood on the Clocktower."""
    
    __tablename__ = 'games'
    
    # Statuts de partie
    SETUP = 'setup'
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'
    
    # Phases de jeu
    DAY = 'day'
    NIGHT = 'night'
    
    # Gagnants
    GOOD = 'good'
    EVIL = 'evil'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    edition_id = db.Column(db.Integer, db.ForeignKey('editions.id'), nullable=False)
    
    # État de la partie
    status = db.Column(db.String(20), default=SETUP)
    current_phase = db.Column(db.String(10))  # 'day' ou 'night'
    current_day_number = db.Column(db.Integer, default=0)
    current_night_number = db.Column(db.Integer, default=0)
    
    # Joueurs
    player_count = db.Column(db.Integer, nullable=False)
    
    # Résultat
    winner = db.Column(db.String(10))  # 'good', 'evil', ou null
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime)
    ended_at = db.Column(db.DateTime)
    
    # Notes du conteur
    storyteller_notes = db.Column(db.Text)
    
    # Relations
    edition = db.relationship('Edition', back_populates='games')
    players = db.relationship('Player', back_populates='game', lazy='dynamic', cascade='all, delete-orphan')
    night_actions = db.relationship('NightAction', back_populates='game', lazy='dynamic', cascade='all, delete-orphan')
    day_actions = db.relationship('DayAction', back_populates='game', lazy='dynamic', cascade='all, delete-orphan')
    reminder_tokens = db.relationship('ReminderToken', back_populates='game', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Game {self.name} ({self.status})>'
    
    def start_game(self):
        """Démarre la partie (passe de setup à in_progress)."""
        if self.status == self.SETUP:
            self.status = self.IN_PROGRESS
            self.started_at = datetime.utcnow()
            self.current_phase = self.NIGHT
            self.current_night_number = 1
    
    def end_game(self, winner: str):
        """Termine la partie."""
        self.status = self.FINISHED
        self.winner = winner
        self.ended_at = datetime.utcnow()
    
    def next_phase(self):
        """Passe à la phase suivante (jour -> nuit ou nuit -> jour)."""
        if self.current_phase == self.NIGHT:
            self.current_phase = self.DAY
            self.current_day_number += 1
        else:
            self.current_phase = self.NIGHT
            self.current_night_number += 1


class Player(db.Model):
    """Joueurs dans une partie."""
    
    __tablename__ = 'players'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    seat_position = db.Column(db.Integer, nullable=False)  # Position dans le cercle (1-15)
    
    # Rôle
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    alignment = db.Column(db.String(10), nullable=False)  # 'good' ou 'evil'
    
    # État
    is_alive = db.Column(db.Boolean, default=True)
    used_dead_vote = db.Column(db.Boolean, default=False)
    death_night = db.Column(db.Integer)  # Numéro de la nuit de mort
    death_day = db.Column(db.Integer)  # Numéro du jour de mort
    
    # États spéciaux
    is_poisoned = db.Column(db.Boolean, default=False)
    is_drunk = db.Column(db.Boolean, default=False)
    is_protected = db.Column(db.Boolean, default=False)
    
    # Notes du conteur
    notes = db.Column(db.Text)
    
    # Métadonnées
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    game = db.relationship('Game', back_populates='players')
    character = db.relationship('Character', back_populates='players')
    reminder_tokens = db.relationship('ReminderToken', back_populates='player', lazy='dynamic', cascade='all, delete-orphan')
    
    # Actions effectuées
    night_actions_made = db.relationship(
        'NightAction',
        foreign_keys='NightAction.player_id',
        back_populates='player',
        lazy='dynamic'
    )
    night_actions_received = db.relationship(
        'NightAction',
        foreign_keys='NightAction.target_player_id',
        back_populates='target_player',
        lazy='dynamic'
    )
    
    def __repr__(self):
        return f'<Player {self.name} ({self.character.name if self.character else "?"})>'
    
    def kill(self, night_number: Optional[int] = None, day_number: Optional[int] = None):
        """Tue le joueur."""
        self.is_alive = False
        if night_number:
            self.death_night = night_number
        if day_number:
            self.death_day = day_number


class NightAction(db.Model):
    """Actions effectuées pendant la nuit."""
    
    __tablename__ = 'night_actions'
    
    # Types d'actions
    KILL = 'kill'
    PROTECT = 'protect'
    POISON = 'poison'
    CHECK = 'check'
    INFO = 'info'
    SPECIAL = 'special'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    night_number = db.Column(db.Integer, nullable=False)
    
    # Qui fait l'action
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    
    # Type d'action
    action_type = db.Column(db.String(20), nullable=False)
    
    # Cible (optionnel selon l'action)
    target_player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    
    # Résultat (format JSON pour résultats complexes)
    # Exemples: {"demon": true}, {"count": 2}, {"character": "Imp"}
    result = db.Column(db.JSON)
    
    # Notes
    notes = db.Column(db.Text)
    
    # Timestamp
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    game = db.relationship('Game', back_populates='night_actions')
    character = db.relationship('Character')
    player = db.relationship('Player', foreign_keys=[player_id], back_populates='night_actions_made')
    target_player = db.relationship('Player', foreign_keys=[target_player_id], back_populates='night_actions_received')
    
    def __repr__(self):
        return f'<NightAction {self.action_type} by {self.player_id} on night {self.night_number}>'


class DayAction(db.Model):
    """Actions effectuées pendant le jour (nominations, votes, exécutions)."""
    
    __tablename__ = 'day_actions'
    
    # Types d'actions
    NOMINATION = 'nomination'
    VOTE = 'vote'
    EXECUTION = 'execution'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    action_type = db.Column(db.String(20), nullable=False)
    
    # Nomination
    nominator_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    nominee_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    
    # Vote
    vote_count = db.Column(db.Integer)  # Nombre de votes pour
    votes_against = db.Column(db.Integer)  # Nombre de votes contre
    
    # Résultat
    executed = db.Column(db.Boolean, default=False)
    
    # Notes
    notes = db.Column(db.Text)
    
    # Timestamp
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    game = db.relationship('Game', back_populates='day_actions')
    nominator = db.relationship('Player', foreign_keys=[nominator_id])
    nominee = db.relationship('Player', foreign_keys=[nominee_id])
    
    def __repr__(self):
        return f'<DayAction {self.action_type} on day {self.day_number}>'


class ReminderToken(db.Model):
    """Tokens de rappel pour le conteur."""
    
    __tablename__ = 'reminder_tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))  # Optionnel (peut être global)
    
    # Type et description
    token_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    
    # État
    is_active = db.Column(db.Boolean, default=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    game = db.relationship('Game', back_populates='reminder_tokens')
    player = db.relationship('Player', back_populates='reminder_tokens')
    
    def __repr__(self):
        return f'<ReminderToken {self.token_type}>'

