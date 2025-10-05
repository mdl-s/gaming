# 🚀 Guide de Démarrage - Version 1.5.0

## 🎉 Bienvenue dans Blood on the Clocktower v1.5 !

Cette version inclut le **bug fix majeur** et les **fonctionnalités Phase 2** !

---

## ⚡ Démarrage Rapide

### 1. Lancer l'Application

```bash
cd /Users/michael/development/gaming/blood-on-clocktower
source venv/bin/activate
python run.py
```

**Accès** : http://localhost:5002

### 2. Créer Votre Première Partie

1. **Page d'accueil** → Cliquer sur **"Nouvelle Partie"**
2. **Nom** : "Ma première partie"
3. **Édition** : Trouble Brewing
4. **Joueurs** : 7 (recommandé pour commencer)
5. **Cliquer** "Créer la Partie"

### 3. Configurer les Joueurs

1. **Entrer les 7 noms** (ex: Alice, Bob, Charlie, Diana, Eve, Frank, Grace)
2. **Cliquer** "Distribuer les Rôles"
3. **NOUVEAU** : Vous verrez un gros bouton vert **"▶️ Démarrer la Partie"**
4. **Cliquer** pour lancer officiellement la partie

### 4. Interface Grimoire

Vous êtes maintenant dans le **Grimoire** !

#### Vue Circulaire
- **7 cartes** affichant chaque joueur avec :
  - Nom
  - Rôle secret (Townsfolk, Outsider, Minion, Demon)
  - Position dans le cercle
  - Statut vivant/mort
  - États spéciaux (🧪 empoisonné, 🍺 ivre)

#### Actions Rapides
- **Bouton Tuer** → Marque le joueur comme mort
- **Bouton Poison** → Marque le joueur comme empoisonné
- **Cliquer sur un joueur** → Voir détails complets

#### Navigation
- **📜 Historique** → Voir la timeline complète
- **Passer au Jour/Nuit** → Changer de phase
- **Terminer la Partie** → Déclarer le gagnant

---

## 🌙 Phase de Nuit

### Ordre de Nuit Automatique

**Panneau de droite** affiche l'ordre correct :
- **Première Nuit** : Ordre spécial pour setup
- **Autres Nuits** : Ordre standard

### Déroulement

1. **Consulter l'ordre** dans le panneau
2. **Réveiller chaque personnage** dans l'ordre
3. **Enregistrer les actions** :
   - Qui tue l'Imp ? → Cliquer "Tuer" sur la victime
   - Qui empoisonne le Poisoner ? → Cliquer "Poison"
   - Etc.

4. **Passer au Jour** quand terminé

---

## ☀️ Phase de Jour

### Nouvelle Fonctionnalité : Nominations et Votes

#### Créer une Nomination

1. **Panneau "Nominations du Jour"** apparaît
2. **Cliquer** sur **"+ Nouvelle Nomination"**
3. **Modal s'ouvre** :
   - Sélectionner le **nominateur** (qui nomine)
   - Sélectionner le **nominé** (qui est nominé)
4. **Valider** → Nomination enregistrée

#### Enregistrer les Votes

1. **Liste des nominations** affiche chaque nomination
2. **Cliquer** sur **"📊 Enregistrer les Votes"**
3. **Modal de vote** s'ouvre :
   - **Votes POUR** : Nombre de mains levées
   - **Votes CONTRE** : Nombre contre (optionnel)
   - **Majorité requise** : Affichée automatiquement
   - **Checkbox "Exécution"** : Cocher si majorité atteinte
   - **Notes** : Commentaires optionnels
4. **Valider** → Si "Exécution" cochée, le joueur est **automatiquement tué** 💀

#### Exemple Complet

```
Jour 1 : 7 joueurs vivants → Majorité = 4 votes

Nomination 1:
- Alice nomine Bob
- Votes: 3 POUR, 4 CONTRE
- Résultat: Bob survit

Nomination 2:
- Charlie nomine Diana
- Votes: 5 POUR, 2 CONTRE
- ✓ Exécution cochée
- Résultat: Diana est tuée automatiquement 💀
```

### Passer à la Nuit

**Cliquer** sur **"Passer à la Nuit →"** quand les discussions sont terminées

---

## 📜 Historique Détaillé

### Consulter l'Historique

**Depuis le Grimoire**, cliquer sur **"📜 Historique"**

### Contenu Affiché

#### Timeline Chronologique

**Nuit 1** (fond violet)
- Actions de nuit enregistrées
- Qui a fait quoi, sur qui
- Résultats

**Jour 1** (fond jaune)
- Toutes les nominations
- Résultats de chaque vote
- Exécutions

**Nuit 2**, **Jour 2**, etc.

#### Fin de Partie

**Bannière finale** indiquant :
- 🏁 Fin de Partie
- 👑 Victoire du Bien ou 💀 Victoire du Mal
- Date et heure de fin

### Fonctionnalités

- **Impression** : Bouton 🖨️ pour imprimer la timeline
- **Navigation** : Retour au Grimoire à tout moment
- **Recherche visuelle** : Code couleur nuit/jour

---

## 🎯 Workflow Complet d'une Partie

### Étape 1 : Setup (5 min)
1. Créer la partie
2. Entrer les noms
3. Distribuer les rôles
4. **Démarrer la partie** ✨

### Étape 2 : Première Nuit (10 min)
1. Ouvrir le Grimoire
2. Suivre l'ordre de nuit affiché
3. Réveiller chaque joueur dans l'ordre
4. Enregistrer les actions (poison, kill, etc.)
5. Passer au Jour 1

### Étape 3 : Jour 1 (20 min)
1. Discussions libres entre joueurs
2. Créer des nominations avec le modal
3. Voter et enregistrer les résultats
4. Exécuter si majorité
5. Passer à la Nuit 2

### Étape 4 : Nuits/Jours Suivants
- Répéter le cycle
- Consulter l'historique si besoin
- Suivre les vivants/morts dans le Grimoire

### Étape 5 : Fin de Partie
1. Déterminer le gagnant (Bien ou Mal)
2. Cliquer "Terminer la Partie"
3. Sélectionner le gagnant
4. Consulter l'historique complet
5. Imprimer si souhaité

---

## 💡 Astuces et Conseils

### Pour les Conteurs Débutants

1. **Préparez-vous** : Lisez les capacités des personnages avant
2. **Ordre de nuit** : Utilisez le panneau, ne le mémorisez pas
3. **Historique** : Consultez-le entre les phases pour vous rappeler
4. **Notes** : Cliquez sur un joueur pour ajouter des notes privées

### Fonctionnalités Cachées

- **Cliquer sur un joueur** → Page de détails avec notes
- **Historique** → Disponible à tout moment
- **Badges** → Code couleur visuel (Bleu=Bon, Rouge=Mal, Gris=Mort)
- **Compteur automatique** → Calcul de la majorité dans les votes

### Raccourcis

| Action | Méthode |
|--------|---------|
| Tuer rapidement | Bouton "Tuer" sur la carte |
| Empoisonner | Bouton "Poison" sur la carte |
| Voir détails | Cliquer sur la carte joueur |
| Historique | Bouton "📜 Historique" en haut |
| Changer phase | Bouton bleu central |

---

## 🆘 Problèmes Courants

### "La partie n'a pas encore été démarrée"

**Solution** : Après distribution des rôles, cliquez sur le bouton vert **"▶️ Démarrer la Partie"** sur la page de détails.

### Les nominations ne s'affichent pas

**Vérification** : Les nominations n'apparaissent que pendant la **Phase de Jour**. Vérifiez l'en-tête du Grimoire (☀️ Jour X).

### Je ne peux pas voter

**Explication** : Les votes se font via le modal **"📊 Enregistrer les Votes"**. Le Conteur compte les mains levées et entre le résultat.

### L'historique est vide

**Explication** : L'historique se remplit au fur et à mesure. Si vous venez de commencer, il sera vide jusqu'à ce que des actions soient enregistrées.

---

## 📊 Différences vs Version 1.0

### Ce qui a changé

| Fonctionnalité | v1.0 | v1.5 |
|----------------|------|------|
| Après distribution rôles | ❌ Bloqué | ✅ Bouton "Démarrer" |
| Nominations | ❌ Manquait | ✅ Modal complet |
| Votes | ❌ Manquait | ✅ Comptage détaillé |
| Historique | ❌ Basique | ✅ Timeline complète |
| API Actions Nuit | ❌ Non | ✅ Oui (POST) |
| Interface | ⚠️ Correct | ✅ Élégante |

### Fonctionnalités Ajoutées

- ✨ Modal de nomination
- ✨ Modal de vote avec comptage
- ✨ Page d'historique dédiée
- ✨ Bouton historique dans Grimoire
- ✨ Fonction impression
- ✨ API actions de nuit
- ✨ Exécution automatique
- ✨ Badges de statut
- ✨ Notes sur votes

---

## 🎓 Pour Aller Plus Loin

### Documentation Complète

- **README.md** : Vue d'ensemble
- **PHASE2_UPDATE.md** : Détails techniques des nouveautés
- **CHANGELOG.md** : Historique des versions
- **ARCHITECTURE.md** : Structure technique

### Développement Futur

**Phase 2 (en cours)** :
- Export JSON/PDF
- Statistiques avancées
- UI actions de nuit

**Phase 3 (à venir)** :
- Bad Moon Rising
- Sects & Violets
- Scripts personnalisés
- Mode multi-Conteur

---

## 🙏 Feedback

Si vous rencontrez des problèmes ou avez des suggestions :

1. Consultez les logs dans le terminal
2. Vérifiez le CHANGELOG.md
3. Lisez PHASE2_UPDATE.md pour les détails techniques

---

## 🎉 Profitez !

**Votre application est maintenant prête pour gérer des parties complètes de Blood on the Clocktower !**

**Bon jeu ! 🎭**

---

**Version** : 1.5.0  
**Date** : 5 octobre 2025  
**Statut** : ✅ Production Ready

