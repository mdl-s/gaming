# 📦 Guide d'Installation Détaillé

Ce guide vous aidera à installer et démarrer l'application Blood on the Clocktower.

## ✅ Prérequis

Avant de commencer, assurez-vous d'avoir :

- **Python 3.10 ou supérieur** installé ([Télécharger Python](https://www.python.org/downloads/))
- **pip** (installé automatiquement avec Python)
- Un terminal/ligne de commande
- Un navigateur web moderne

## 🚀 Installation Pas à Pas

### Étape 1 : Préparation de l'Environnement

```bash
# Naviguer vers le dossier du projet
cd blood-on-clocktower

# Créer un environnement virtuel Python
python -m venv venv

# Activer l'environnement virtuel

# Sur macOS/Linux :
source venv/bin/activate

# Sur Windows (CMD) :
venv\Scripts\activate

# Sur Windows (PowerShell) :
venv\Scripts\Activate.ps1
```

Vous devriez voir `(venv)` apparaître au début de votre ligne de commande.

### Étape 2 : Installation des Dépendances

```bash
# Installer toutes les dépendances requises
pip install -r requirements.txt
```

Cela installera :
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.0.5
- python-dotenv 1.0.0

### Étape 3 : Initialisation de la Base de Données

```bash
# Initialiser Flask-Migrate (une seule fois)
flask db init

# Créer la première migration
flask db migrate -m "Initial migration"

# Appliquer les migrations à la base de données
flask db upgrade
```

### Étape 4 : Peupler la Base de Données

```bash
# Exécuter le script de seed pour ajouter les personnages de Trouble Brewing
python seed_data.py
```

Vous devriez voir :
```
🗑️  Nettoyage de la base de données...
📚 Création de l'édition Trouble Brewing...
👥 Ajout des Villageois...
🎭 Ajout des Étrangers...
😈 Ajout des Sbires...
👹 Ajout du Démon...

✅ Base de données peuplée avec succès !
   - 1 édition créée
   - 13 Villageois
   - 4 Étrangers
   - 4 Sbires
   - 1 Démon
   Total : 22 personnages
```

### Étape 5 : Lancer l'Application

```bash
# Démarrer le serveur Flask
python run.py
```

Vous verrez :
```
 * Running on http://127.0.0.1:5002
 * Running on http://0.0.0.0:5002
```

### Étape 6 : Accéder à l'Application

Ouvrez votre navigateur et allez à :
```
http://localhost:5002
```

## 🎉 C'est Parti !

Vous devriez maintenant voir la page d'accueil de l'application. Vous pouvez :

1. **Créer une nouvelle partie** via le bouton "Nouvelle Partie"
2. **Consulter les personnages** dans la section "Personnages"
3. **Lire les règles** dans la section "Règles"

## 🛠️ Commandes Utiles

### Arrêter le Serveur
Appuyez sur `Ctrl + C` dans le terminal

### Désactiver l'Environnement Virtuel
```bash
deactivate
```

### Réactiver l'Environnement Virtuel
```bash
# Sur macOS/Linux
source venv/bin/activate

# Sur Windows
venv\Scripts\activate
```

### Réinitialiser la Base de Données
```bash
# Supprimer la base de données existante
rm instance/botc.db

# Recréer et peupler
flask db upgrade
python seed_data.py
```

### Voir les Logs en Mode Debug
Le mode debug est activé par défaut en développement. Les erreurs s'affichent directement dans le navigateur.

## 🐛 Résolution de Problèmes

### Erreur : "python: command not found"
- Essayez `python3` au lieu de `python`
- Vérifiez que Python est bien installé : `python --version`

### Erreur : "No module named 'flask'"
- Assurez-vous que l'environnement virtuel est activé (vous devez voir `(venv)`)
- Réinstallez les dépendances : `pip install -r requirements.txt`

### Erreur : "Address already in use"
- Le port 5002 est déjà utilisé
- Tuez le processus ou changez le port dans `run.py` :
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)
  ```

### La Page ne se Charge Pas
- Vérifiez que le serveur est bien démarré
- Essayez `http://127.0.0.1:5002` au lieu de `localhost:5002`
- Consultez les logs dans le terminal

### Erreur de Base de Données
- Supprimez le dossier `instance/` et recommencez l'étape 3
- Vérifiez les permissions d'écriture dans le dossier du projet

## 📞 Besoin d'Aide ?

Si vous rencontrez des problèmes non listés ici :

1. Vérifiez que toutes les étapes ont été suivies dans l'ordre
2. Consultez les logs d'erreur dans le terminal
3. Vérifiez votre version de Python : `python --version` (doit être ≥ 3.10)
4. Assurez-vous d'avoir les droits d'écriture dans le dossier

## 🎯 Prochaines Étapes

Une fois l'installation réussie :

1. Lisez le [README.md](README.md) pour comprendre les fonctionnalités
2. Consultez la section "Règles" de l'application
3. Créez votre première partie test avec 7 joueurs
4. Explorez l'interface Grimoire

**Bon jeu !** 🎭

