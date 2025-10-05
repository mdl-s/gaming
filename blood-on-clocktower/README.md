# 🕐 Blood on the Clocktower - Gestionnaire de Partie

Application web complète pour gérer des parties de **Blood on the Clocktower** en tant que Conteur.

## 🎯 Fonctionnalités

### ✅ Phase 1 (MVP) - Terminée

- **Gestion des parties**
  - Créer une nouvelle partie
  - Sélectionner l'édition (Trouble Brewing)
  - Ajouter des joueurs (5-15 joueurs)
  - Distribution automatique des rôles
  - Démarrage de partie en un clic
  
- **Interface Grimoire**
  - Vue circulaire des joueurs avec leurs rôles
  - Statut vivant/mort de chaque joueur
  - Marqueurs d'état (empoisonné, ivre)
  - Actions rapides (tuer, empoisonner)
  
- **Gestion des phases**
  - Alternance jour/nuit
  - Ordre de nuit automatique (première nuit / autres nuits)
  - Interface de fin de partie
  
- **Base de données complète**
  - 22 personnages de Trouble Brewing
  - Descriptions et ordres de nuit
  - Tokens de rappel

### 🚀 Phase 2 (Améliorations) - Terminée ✅

- **Système de nominations et votes** ✅
  - Modal de nomination avec sélection facile
  - Modal de vote avec comptage POUR/CONTRE
  - Calcul automatique de la majorité
  - Exécution automatique
  - Liste des nominations du jour
  
- **Historique détaillé** ✅
  - Timeline complète nuit par nuit
  - Tous les événements enregistrés
  - Page dédiée avec impression
  - Navigation facile depuis Grimoire
  
- **API Actions de nuit** ✅
  - Enregistrement structuré des actions
  - Support tous types d'actions

### 🌟 Phase 3 (Éditions Avancées) - Terminée ✅

- **Bad Moon Rising** ✅ (25 personnages)
  - Édition intermédiaire (★★☆)
  - Morts multiples la nuit
  - Mécaniques de résurrection
  - 4 Démons différents
  
- **Sects & Violets** ✅ (25 personnages)
  - Édition avancée (★★★)
  - Mécaniques de folie (mad)
  - Transformations de personnages
  - Capacités complexes
  
- **Travellers** ✅ (15 personnages)
  - Personnages itinérants
  - Pour toutes les éditions
  - Modificateurs de jeu
  
- **Scripts Personnalisés** ✅
  - Interface de création
  - Sélection multi-éditions
  - Filtres par type
  
**Total : 87 personnages disponibles !**

## 🚀 Installation

### Prérequis

- Python 3.10 ou supérieur
- pip

### Étapes d'installation

1. **Cloner le projet**
```bash
cd blood-on-clocktower
```

2. **Créer un environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Initialiser la base de données**
```bash
# Créer les tables
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Peupler avec les données de Trouble Brewing
python seed_data.py
```

5. **Lancer l'application**
```bash
python run.py
```

L'application sera accessible sur `http://localhost:5002`

## 📚 Structure du Projet

```
blood-on-clocktower/
├── app/
│   ├── __init__.py          # Factory Flask
│   ├── models.py            # Modèles SQLAlchemy
│   ├── config.py            # Configuration
│   ├── blueprints/
│   │   ├── main/            # Pages principales
│   │   ├── game/            # Gestion des parties
│   │   ├── grimoire/        # Interface Grimoire
│   │   └── admin/           # Administration
│   ├── static/              # CSS, JS, images
│   └── templates/           # Templates HTML
├── instance/                # Base de données SQLite
├── migrations/              # Migrations Alembic
├── requirements.txt         # Dépendances Python
├── run.py                   # Point d'entrée
└── seed_data.py            # Script de peuplement DB
```

## 🎮 Utilisation

### Créer une nouvelle partie

1. Cliquez sur "Nouvelle Partie"
2. Entrez le nom de la partie
3. Sélectionnez l'édition (Trouble Brewing)
4. Choisissez le nombre de joueurs (5-15)
5. Entrez les noms des joueurs
6. Les rôles sont distribués automatiquement

### Utiliser le Grimoire

- **Vue circulaire** : Tous les joueurs avec leur rôle et position
- **Actions rapides** : Tuer, empoisonner, ressusciter un joueur
- **Phases** : Alternez entre jour et nuit
- **Ordre de nuit** : Liste des personnages à réveiller dans l'ordre
- **Fin de partie** : Déclarez le gagnant (Bien ou Mal)

### Consulter les personnages

- Allez dans "Personnages" pour voir tous les rôles disponibles
- Filtrez par édition
- Consultez les capacités et ordres de nuit

## 🛠️ Technologies Utilisées

- **Backend** : Flask 3.0, Python 3.10+
- **ORM** : Flask-SQLAlchemy
- **Base de données** : SQLite (évolutif vers PostgreSQL)
- **Frontend** : HTML5, Tailwind CSS via CDN
- **Icons** : Lucide Icons
- **Architecture** : Blueprints Flask modulaires

## 📋 Roadmap

### Phase 2 - Améliorations (À venir)
- [ ] Historique détaillé des actions
- [ ] Export de parties (JSON/PDF)
- [ ] Système de nominations et votes complet
- [ ] Statistiques de parties
- [ ] Actions de nuit enregistrées

### Phase 3 - Extensions (Futur)
- [ ] Autres éditions (Bad Moon Rising, Sects & Violets)
- [ ] Scripts personnalisés
- [ ] Mode multi-Conteur
- [ ] Timer intégré

## 🎯 Distribution des Rôles

| Joueurs | Villageois | Étrangers | Sbires | Démon |
|---------|------------|-----------|--------|-------|
| 5       | 3          | 0         | 1      | 1     |
| 6       | 3          | 1         | 1      | 1     |
| 7       | 5          | 0         | 1      | 1     |
| 8       | 5          | 1         | 1      | 1     |
| 9       | 5          | 2         | 1      | 1     |
| 10      | 7          | 0         | 2      | 1     |
| 11      | 7          | 1         | 2      | 1     |
| 12      | 7          | 2         | 2      | 1     |
| 13      | 9          | 0         | 3      | 1     |
| 14      | 9          | 1         | 3      | 1     |
| 15      | 9          | 2         | 3      | 1     |

**Note** : Si Baron en jeu, remplacer 2 Villageois par 2 Étrangers supplémentaires.

## 🤝 Contribution

Ce projet est personnel mais les suggestions sont bienvenues ! N'hésitez pas à ouvrir une issue pour proposer des améliorations.

## 📝 Licence

Ce projet est à but personnel et éducatif. Blood on the Clocktower est une propriété de The Pandemonium Institute.

## 🙏 Crédits

- **Blood on the Clocktower** créé par Steven Medway et The Pandemonium Institute
- **Application** développée avec ❤️ pour les Conteurs

---

**Bon jeu et que le meilleur camp gagne !** 🎭

