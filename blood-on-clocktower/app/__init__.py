"""Factory pour l'application Flask."""
from flask import Flask
from flask_migrate import Migrate

from app.config import config
from app.models import db


migrate = Migrate()


def create_app(config_name='default'):
    """
    Crée et configure l'application Flask.
    
    Args:
        config_name: Nom de la configuration à utiliser ('development', 'production', 'testing')
    
    Returns:
        Application Flask configurée
    """
    app = Flask(__name__)
    
    # Charger la configuration
    app.config.from_object(config[config_name])
    
    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Créer le dossier instance s'il n'existe pas
    import os
    os.makedirs(os.path.join(app.instance_path), exist_ok=True)
    
    # Enregistrer les blueprints
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.blueprints.game import bp as game_bp
    app.register_blueprint(game_bp, url_prefix='/game')
    
    from app.blueprints.grimoire import bp as grimoire_bp
    app.register_blueprint(grimoire_bp, url_prefix='/grimoire')
    
    from app.blueprints.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Contexte du shell
    @app.shell_context_processor
    def make_shell_context():
        from app.models import Edition, Character, Game, Player, NightAction, DayAction, ReminderToken
        return {
            'db': db,
            'Edition': Edition,
            'Character': Character,
            'Game': Game,
            'Player': Player,
            'NightAction': NightAction,
            'DayAction': DayAction,
            'ReminderToken': ReminderToken
        }
    
    return app

