# 📋 TODO List - Blood on the Clocktower

## ✅ Phase 1 - MVP (TERMINÉ)

### Gestion des Parties
- [x] Créer une nouvelle partie
- [x] Sélectionner l'édition (Trouble Brewing)
- [x] Ajouter/retirer des joueurs avec noms
- [x] Positionner les joueurs en cercle (ordre des sièges)
- [x] Calcul automatique de la distribution des rôles
- [x] Tirage aléatoire des rôles (avec respect des règles)
- [x] Affichage du Grimoire (tableau de bord du Conteur)

### Interface Grimoire
- [x] Vue circulaire des joueurs avec leurs positions
- [x] Affichage du rôle réel de chaque joueur
- [x] Statut vivant/mort de chaque joueur
- [x] Marqueurs d'état (empoisonné, ivre)
- [x] Actions rapides (tuer, ressusciter, empoisonner)
- [x] Notes libres sur chaque joueur

### Gestion des Phases
- [x] Alternance automatique Jour/Nuit
- [x] Ordre de nuit (première nuit / autres nuits)
- [x] Interface de fin de partie
- [x] Compteurs de jours/nuits

### Base de Données
- [x] 22 personnages Trouble Brewing
- [x] Descriptions complètes
- [x] Ordres de nuit corrects
- [x] Tokens de rappel

## 🚧 Phase 2 - Améliorations (PROCHAIN)

### Système de Votes et Nominations
- [ ] Interface de nomination complète
- [ ] Système de vote avec comptage en temps réel
- [ ] Gestion des exécutions
- [ ] Historique des nominations de la journée
- [ ] Tracker des votes morts utilisés
- [ ] Vote du Butler (dépend du maître)

### Historique et Logs
- [ ] Journal de partie détaillé
- [ ] Historique nuit par nuit
- [ ] Historique jour par jour
- [ ] Timeline complète de la partie
- [ ] Export en JSON
- [ ] Export en PDF

### Actions de Nuit
- [ ] Formulaires pour enregistrer les choix des joueurs
  - [ ] Qui tue l'Imp
  - [ ] Qui protège le Monk
  - [ ] Qui empoisonne le Poisoner
  - [ ] Qui vérifie la Fortune Teller
  - [ ] Etc. pour chaque personnage
- [ ] Enregistrement automatique dans NightAction
- [ ] Historique des actions de nuit par joueur

### Système de Rappels Avancé
- [ ] Rappels automatiques selon les rôles en jeu
- [ ] Alertes pour capacités spéciales (Virgin nominé, Slayer utilisé)
- [ ] Notifications en temps réel
- [ ] Checklist interactive pour l'ordre de nuit
- [ ] Timer optionnel pour gérer le rythme

### Conditions de Victoire Automatiques
- [ ] Détection automatique de fin de partie
  - [ ] 2 joueurs ou moins vivants
  - [ ] Mayor avec 3 joueurs
  - [ ] Saint exécuté
  - [ ] Démon exécuté
- [ ] Suggestions au Conteur
- [ ] Vérification des edge cases

### Statistiques
- [ ] Taux de victoire par rôle
- [ ] Taux de victoire par équipe
- [ ] Statistiques par joueur
- [ ] Durée moyenne des parties
- [ ] Graphiques et visualisations

### Personnalisation et Scripts
- [ ] Scripts personnalisés (sélection manuelle des rôles)
- [ ] Import/Export de scripts
- [ ] Validation des scripts custom
- [ ] Bibliothèque de scripts communautaires

### UX/UI Améliorations
- [ ] Drag & Drop pour réorganiser joueurs
- [ ] Keyboard shortcuts pour navigation rapide
- [ ] Tooltips interactifs sur tous les personnages
- [ ] Vue mobile optimisée
- [ ] Mode tutoriel interactif
- [ ] Animations et transitions fluides

### Fonctionnalités du Conteur
- [ ] Undo/Redo pour actions critiques
- [ ] Backup/autosave régulier
- [ ] Restauration de partie en cas d'erreur
- [ ] Notes globales sur la partie
- [ ] Système de bookmarks pour moments clés

## 🔮 Phase 3 - Extensions (FUTUR)

### Autres Éditions
- [ ] Bad Moon Rising
  - [ ] 20 nouveaux personnages
  - [ ] Mécaniques spécifiques
  - [ ] Ordre de nuit adapté
- [ ] Sects & Violets
  - [ ] 20 nouveaux personnages
  - [ ] Mécaniques complexes
  - [ ] Ordre de nuit adapté
- [ ] Experimental Characters

### Travellers
- [ ] Support des Travellers (personnages spéciaux)
- [ ] Ajout/retrait en cours de partie
- [ ] Votes spéciaux des Travellers
- [ ] Exil des Travellers

### Fonctionnalités Avancées
- [ ] Mode multi-Conteur (collaboration)
- [ ] Mode spectateur pour stream
- [ ] Intégration timer/chronomètre
- [ ] Intégration audio/musique d'ambiance
- [ ] Support des Fabled (personnages modificateurs)
- [ ] Mode "Atheist" (pas de Démon)
- [ ] Support des scripts officiels Kickstarter

### Technique
- [ ] Migration vers PostgreSQL (production)
- [ ] API REST pour intégrations externes
- [ ] Authentification utilisateurs (multi-Conteur)
- [ ] WebSockets pour updates temps réel
- [ ] Mode hors-ligne (Progressive Web App)
- [ ] App mobile native (React Native?)

### Thèmes et Personnalisation
- [ ] Thèmes UI personnalisables
- [ ] Mode clair/sombre toggle
- [ ] Langue française/anglaise
- [ ] Images personnalisées pour personnages
- [ ] Sons personnalisés

### Communauté
- [ ] Partage de parties (liens publics)
- [ ] Replay de parties passées
- [ ] Commentaires post-partie
- [ ] Notation des parties
- [ ] Forum/discussions intégrés

## 🐛 Bugs Connus

- [ ] Aucun pour le moment

## 💡 Idées en Vrac

- [ ] Mode "Night Order Helper" avec notifications sonores
- [ ] Générateur aléatoire de scripts équilibrés
- [ ] IA suggérant des bluffs pour le Démon
- [ ] Analyse post-partie avec insights stratégiques
- [ ] Mode entraînement pour nouveaux Conteurs
- [ ] Intégration Discord bot
- [ ] Support des extensions homebrew
- [ ] Marketplace de scripts custom

---

**Priorisé par importance et faisabilité**

