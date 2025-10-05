#!/bin/bash

# Script de démarrage rapide pour Blood on the Clocktower
# Usage: ./start.sh

echo "🕐 Blood on the Clocktower - Démarrage..."
echo ""

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
    echo "✅ Environnement virtuel créé"
    echo ""
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances si nécessaire
if [ ! -f "venv/installed" ]; then
    echo "📥 Installation des dépendances..."
    pip install -r requirements.txt
    touch venv/installed
    echo "✅ Dépendances installées"
    echo ""
fi

# Vérifier si la base de données existe
if [ ! -f "instance/botc.db" ]; then
    echo "🗄️  Initialisation de la base de données..."
    flask db init 2>/dev/null || echo "Migrations déjà initialisées"
    flask db migrate -m "Initial migration" 2>/dev/null || echo "Migration déjà créée"
    flask db upgrade
    
    echo "📚 Peuplement de la base de données..."
    python seed_data.py
    echo ""
fi

echo "🚀 Démarrage du serveur Flask..."
echo "📍 L'application sera accessible sur http://localhost:5000"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Lancer l'application
python run.py

