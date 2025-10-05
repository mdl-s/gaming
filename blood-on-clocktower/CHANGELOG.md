# 📜 Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

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

