# 🚀 Guide de Démarrage Rapide

Vous voulez lancer l'application en 2 minutes ? Suivez ce guide !

## Option 1 : Script Automatique (Recommandé)

### Sur macOS/Linux :
```bash
chmod +x start.sh
./start.sh
```

### Sur Windows :
```cmd
start.bat
```

Le script s'occupe automatiquement de :
- ✅ Créer l'environnement virtuel
- ✅ Installer les dépendances
- ✅ Initialiser la base de données
- ✅ Peupler avec les personnages
- ✅ Lancer le serveur

## Option 2 : Installation Manuelle

```bash
# 1. Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Initialiser la base de données
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 4. Peupler la base de données
python seed_data.py

# 5. Lancer l'application
python run.py
```

## 🌐 Accéder à l'Application

Une fois le serveur démarré, ouvrez votre navigateur :

```
http://localhost:5000
```

## 🎮 Premiers Pas

1. **Créer une partie**
   - Cliquez sur "Nouvelle Partie"
   - Entrez un nom et sélectionnez "Trouble Brewing"
   - Choisissez 7 joueurs (recommandé pour débuter)

2. **Configurer les joueurs**
   - Entrez les noms des 7 joueurs
   - Validez → Les rôles sont distribués automatiquement

3. **Utiliser le Grimoire**
   - Vous voyez maintenant tous les joueurs avec leurs rôles
   - Utilisez "Passer à la Nuit" ou "Passer au Jour"
   - Cliquez sur un joueur pour plus de détails

4. **Gérer la partie**
   - Actions rapides : Tuer, Empoisonner
   - Suivez l'ordre de nuit affiché
   - Terminez la partie en déclarant le gagnant

## 📚 Documentation Complète

- **README.md** : Vue d'ensemble et fonctionnalités
- **INSTALLATION.md** : Guide d'installation détaillé
- **CHANGELOG.md** : Historique des versions

## 🐛 Problèmes ?

### Le serveur ne démarre pas
```bash
# Vérifier Python
python --version  # Doit être >= 3.10

# Réinstaller les dépendances
pip install --upgrade -r requirements.txt
```

### Port déjà utilisé
Modifiez le port dans `run.py` :
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Base de données corrompue
```bash
rm -rf instance/  # Supprimer la base
python seed_data.py  # Recréer
```

## 🎯 Étapes Suivantes

- Consultez les **Règles** dans l'application
- Explorez tous les **Personnages** de Trouble Brewing
- Testez différentes configurations (5 à 15 joueurs)
- Lisez le **README.md** pour les fonctionnalités avancées

---

**Prêt à conter ? Let's go ! 🎭**

