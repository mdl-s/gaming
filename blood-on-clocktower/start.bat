@echo off
REM Script de démarrage rapide pour Windows
REM Usage: start.bat

echo.
echo 🕐 Blood on the Clocktower - Demarrage...
echo.

REM Vérifier si l'environnement virtuel existe
if not exist "venv\" (
    echo 📦 Creation de l'environnement virtuel...
    python -m venv venv
    echo ✅ Environnement virtuel cree
    echo.
)

REM Activer l'environnement virtuel
echo 🔧 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances si nécessaire
if not exist "venv\installed" (
    echo 📥 Installation des dependances...
    pip install -r requirements.txt
    echo. > venv\installed
    echo ✅ Dependances installees
    echo.
)

REM Vérifier si la base de données existe
if not exist "instance\botc.db" (
    echo 🗄️  Initialisation de la base de donnees...
    flask db init 2>nul
    flask db migrate -m "Initial migration" 2>nul
    flask db upgrade
    
    echo 📚 Peuplement de la base de donnees...
    python seed_data.py
    echo.
)

echo 🚀 Demarrage du serveur Flask...
echo 📍 L'application sera accessible sur http://localhost:5000
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.

REM Lancer l'application
python run.py

