"""Configuration de l'application Flask."""
import os
from pathlib import Path

# Dossier de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """Configuration de base."""
    
    # Clé secrète pour les sessions et CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Configuration de la base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{BASE_DIR / "instance" / "botc.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration JSON
    JSON_AS_ASCII = False  # Pour supporter les caractères UTF-8
    
    # Autres configurations
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload


class DevelopmentConfig(Config):
    """Configuration pour le développement."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configuration pour la production."""
    DEBUG = False
    TESTING = False
    
    # Override SECRET_KEY - must be set in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY environment variable must be set in production")
    
    # Use PostgreSQL in production if DATABASE_URL is provided
    # Otherwise, fall back to SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{BASE_DIR / "instance" / "botc.db"}'


class TestingConfig(Config):
    """Configuration pour les tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Dictionnaire des configurations
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

