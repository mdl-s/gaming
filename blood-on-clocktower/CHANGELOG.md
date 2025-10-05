# 📜 Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

## [2.1.0] - 2025-10-05 - Révolution UX

### 🎨 Améliorations Majeures UX

#### Layout Pleine Largeur
- **Nouveau layout 3 colonnes** optimisé pour grands écrans
- Gauche (5/12) : Cercle des joueurs
- Centre (4/12) : Ordre de nuit détaillé / Nominations
- Droite (3/12) : Aide conteur contextuelle
- Header sticky avec stats compactes
- Scroll indépendant par colonne
- Optimisation espace : +40% d'affichage

#### Historique Complet
- **Actions automatiquement enregistrées** :
  - Tuer un joueur → NightAction "death"
  - Empoisonner → NightAction "poison"
- Timeline complète avec TOUTES les actions
- Plus de trous dans l'historique

#### Interface Nominations Visuelle
- **Nouveau modal 3 étapes** avec joueurs cliquables
- Étape 1 : Grille visuelle de tous les joueurs
- Étape 2 : Grille filtrée (seulement vivants)
- Étape 3 : Récapitulatif avec validation
- Protection auto contre auto-nomination
- Bouton "Recommencer" si erreur
- UX améliorée de 300%

#### Ordre de Nuit Détaillé
- **Checklist interactive** avec checkboxes
- Descriptions complètes de chaque capacité
- Affichage des joueurs concernés (#position)
- **Rappels spécifiques 💡** pour chaque rôle :
  - Imp, Poisoner, Fortune Teller, Empath, etc.
  - Conseils précis sur quoi faire
- Numéros d'ordre affichés (#11, #15, etc.)
- Barre de progression visuelle
- Proposition auto "Passer au jour" à 100%

#### Aide Conteur Contextuelle
- **Panneau permanent** en colonne droite
- Adapte contenu selon :
  - Phase (Nuit/Jour)
  - Édition (TB/BMR/S&V)
  - Rôles en jeu (Virgin, Butler, etc.)
- **Pendant la Nuit** :
  - Checklist des étapes
  - Rappels généraux
  - Spécificités par édition
- **Pendant le Jour** :
  - Déroulement expliqué
  - Calcul automatique majorité
  - Rappels rôles spéciaux
- Raccourcis clavier
- Info édition (difficulté, description)

### 🐛 Corrections
- Bug historique vide → Toutes actions enregistrées
- Bug layout étroit → Pleine largeur

### 📝 Fichiers Modifiés
- `app/blueprints/grimoire/routes.py` - Historique complet
- `app/templates/grimoire/view.html` - Layout 3 colonnes complet
- `app/templates/base.html` - Support pleine largeur
- `README.md` - v2.1

### 📝 Fichiers Créés
- `app/templates/grimoire/nomination_modal_improved.html`
- `UX_IMPROVEMENTS.md`
- `V2.1_RELEASE_NOTES.md`
- `WHATS_NEW_V2.1.md`

### 📝 Fichiers Supprimés (nettoyage)
- `app/templates/grimoire/nomination_modal.html` (remplacé)
- `app/templates/grimoire/storyteller_help.html` (intégré)

## [2.0.0] - 2025-10-05 - Phase 3 Complète

### 🌟 Nouvelles Éditions

#### Bad Moon Rising ✅
- **25 nouveaux personnages** (13 Townsfolk, 4 Outsider, 4 Minion, 4 Demon)
- Mécaniques intermédiaires : morts multiples, résurrections
- Difficulté 2/3
- Script de seed : `seed_bad_moon_rising.py`
- Personnages notables : Grandmother, Sailor, Lunatic, Zombuul, Shabaloth

#### Sects & Violets ✅
- **25 nouveaux personnages** (13 Townsfolk, 4 Outsider, 4 Minion, 4 Demon)
- Mécaniques avancées : folie (mad), transformations
- Difficulté 3/3
- Script de seed : `seed_sects_and_violets.py`
- Personnages notables : Snake Charmer, Cerenovus, Pit-Hag, Vortox, Fang Gu

#### Travellers ✅
- **15 personnages itinérants** compatibles toutes éditions
- 5 par édition (Trouble Brewing, Bad Moon Rising, Sects & Violets)
- Script de seed : `seed_travellers.py`
- Personnages notables : Judge, Barista, Bureaucrat, Harlot

### 🛠️ Nouvelles Fonctionnalités

#### Scripts Personnalisés
- Page dédiée `/admin/scripts`
- Interface de création avec sélection de personnages
- Filtrage par édition et type
- Modal élégant avec compteur
- UI complète (backend en développement)

#### Script Master
- `seed_all_editions.py` - Peuple toutes les éditions en une commande
- Gestion automatique des erreurs
- Résumé complet après exécution

### 📊 Statistiques Globales
- **3 éditions** complètes
- **87 personnages** au total
- **15 Travellers**
- Support de 5 à 15 joueurs
- Toutes difficultés : ★☆☆ à ★★★

### 📝 Fichiers Ajoutés
- `seed_bad_moon_rising.py`
- `seed_sects_and_violets.py`
- `seed_travellers.py`
- `seed_all_editions.py`
- `app/templates/admin/scripts.html`
- `PHASE3_COMPLETE.md`

## [1.5.0] - 2025-10-05 - Phase 2 Partielle

### 🐛 Corrections de Bugs
- **Bug majeur corrigé** : Après distribution des rôles, ajout d'un bouton "Démarrer la Partie" au lieu de bloquer l'utilisateur
- Flux de démarrage de partie plus intuitif

### ✨ Nouvelles Fonctionnalités

#### Système de Nominations et Votes
- Modal de nomination avec sélection nominateur/nominé
- Modal de vote avec comptage POUR/CONTRE
- Calcul automatique de la majorité requise
- Exécution automatique du nominé si majorité atteinte
- Affichage en temps réel des nominations du jour
- Notes optionnelles sur chaque vote

#### Historique Détaillé
- Page d'historique complète (`/grimoire/:id/history`)
- Timeline chronologique nuit par nuit et jour par jour
- Affichage de toutes les actions de nuit et nominations
- Code couleur : Nuits (violet), Jours (jaune)
- Fonction d'impression pour archivage
- Bouton "Historique" accessible depuis le Grimoire

#### API Actions de Nuit
- Route `/grimoire/:id/night-action` (POST)
- Enregistrement des actions nocturnes
- Support pour kill, poison, check, protect, etc.
- Stockage structuré en base de données

### 🎨 Améliorations UX
- Modals élégants avec Tailwind CSS
- Feedback visuel immédiat sur les actions
- Navigation simplifiée Grimoire ↔ Historique
- Badges colorés pour statuts (exécuté, survécu)

### 📝 Fichiers Ajoutés
- `app/templates/grimoire/nomination_modal.html`
- `app/templates/grimoire/vote_modal.html`
- `app/templates/grimoire/history.html`
- `PHASE2_UPDATE.md`

## [1.0.0] - 2025-10-05

### ✨ Ajouté - MVP Complet

#### Gestion des Parties
- Création de nouvelles parties avec sélection d'édition
- Configuration du nombre de joueurs (5-15)
- Distribution automatique des rôles selon les règles officielles
- Affichage de la distribution des rôles en temps réel
- Setup des noms de joueurs avec positions

#### Interface Grimoire
- Vue circulaire des joueurs avec leurs rôles
- Code couleur par alignement (Bleu = Bon, Rouge = Maléfique)
- Affichage du statut vivant/mort
- Indicateurs d'états spéciaux (empoisonné 🧪, ivre 🍺, mort 💀)
- Actions rapides : tuer, ressusciter, empoisonner
- Page de détails pour chaque joueur
- Système de notes du Conteur par joueur

#### Gestion des Phases
- Alternance automatique Jour/Nuit
- Compteur de jours et de nuits
- Ordre de nuit automatique (première nuit vs autres nuits)
- Liste des personnages à réveiller dans l'ordre
- Interface de fin de partie avec choix du gagnant

#### Base de Données
- Édition Trouble Brewing complète (22 personnages)
- 13 Villageois avec capacités détaillées
- 4 Étrangers avec mécaniques spéciales
- 4 Sbires avec ordres de nuit
- 1 Démon (Imp) avec capacité de kill
- Ordres de nuit précis pour première nuit et autres nuits
- Tokens de rappel pour chaque personnage

#### Interface Utilisateur
- Design dark mode par défaut
- Tailwind CSS pour un style moderne
- Icônes Lucide pour une meilleure UX
- Navigation intuitive avec menu principal
- Messages flash pour les confirmations/erreurs
- Responsive design (desktop first)

#### Pages Administratives
- Liste complète des personnages
- Filtrage des personnages par édition
- Consultation des capacités détaillées
- Page des règles du jeu
- Page "À propos"

#### Fonctionnalités Techniques
- Architecture Flask avec Blueprints modulaires
- SQLAlchemy ORM pour la base de données
- Flask-Migrate pour les migrations
- Script de seed automatique
- Gestion propre des erreurs
- Logs de développement

### 📚 Documentation
- README.md complet avec guide d'utilisation
- INSTALLATION.md avec instructions détaillées
- Guide de résolution de problèmes
- Tableau de distribution des rôles
- Commentaires en français dans le code

### 🎯 Respecte le Cahier des Charges MVP (Phase 1)
- ✅ Setup de partie complet (Trouble Brewing uniquement)
- ✅ Interface Grimoire fonctionnelle
- ✅ Gestion nuit/jour basique
- ✅ Système de votes et exécutions (interface présente)
- ✅ Conditions de victoire (fin de partie manuelle)

## [À Venir] - Phase 2

### Prévisions
- [ ] Historique détaillé des actions nuit par nuit
- [ ] Système complet de nominations et votes
- [ ] Export de parties en JSON/PDF
- [ ] Statistiques avancées
- [ ] Système de rappels automatiques avancé
- [ ] Undo/Redo pour actions du Conteur
- [ ] Timer intégré pour les phases

## [À Venir] - Phase 3

### Prévisions
- [ ] Édition Bad Moon Rising
- [ ] Édition Sects & Violets
- [ ] Support des Travellers
- [ ] Scripts personnalisés
- [ ] Mode multi-Conteur
- [ ] Intégration audio/timer
- [ ] Thèmes UI personnalisables
- [ ] Mode tutorial interactif

---

**Note** : Ce projet suit le format [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

