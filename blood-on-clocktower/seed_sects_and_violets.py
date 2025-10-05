"""Script pour ajouter l'édition Sects & Violets."""
from app import create_app, db
from app.models import Edition, Character

def seed_sects_and_violets():
    """Ajoute Sects & Violets et ses personnages."""
    
    app = create_app()
    
    with app.app_context():
        # Vérifier si l'édition existe déjà
        existing = Edition.query.filter_by(name="Sects & Violets").first()
        if existing:
            print("⚠️  Sects & Violets existe déjà !")
            return
        
        # Créer l'édition Sects & Violets
        print("📚 Création de l'édition Sects & Violets...")
        sects = Edition(
            name="Sects & Violets",
            description="L'édition avancée avec des mécaniques de folie, transformation et capacités complexes.",
            difficulty_level=3
        )
        db.session.add(sects)
        db.session.commit()
        
        # Personnages TOWNSFOLK (Villageois)
        print("👥 Ajout des Villageois...")
        townsfolk = [
            {
                'name': 'Clockmaker',
                'ability_description': "Vous commencez en connaissant combien d'étapes séparent le Démon de son Sbire le plus proche (dans le sens horaire).",
                'first_night': 20,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Dreamer',
                'ability_description': "Chaque nuit, choisissez un joueur (pas vous ou les Voyageurs) : vous apprenez 1 bon et 1 mauvais personnage qu'il pourrait être.",
                'first_night': 21,
                'other_nights': 33,
                'remind_tokens': []
            },
            {
                'name': 'Snake Charmer',
                'ability_description': "Chaque nuit, choisissez un joueur vivant : si c'est le Démon, vous et lui échangez vos personnages et alignements.",
                'first_night': 13,
                'other_nights': 10,
                'remind_tokens': []
            },
            {
                'name': 'Mathematician',
                'ability_description': "Chaque nuit, vous apprenez combien de joueurs ont mal fonctionné aujourd'hui à cause de leur capacité.",
                'first_night': None,
                'other_nights': 34,
                'remind_tokens': ['Mal fonctionné']
            },
            {
                'name': 'Flowergirl',
                'ability_description': "Chaque nuit*, vous apprenez si un Démon a voté aujourd'hui.",
                'first_night': None,
                'other_nights': 35,
                'remind_tokens': ['Démon a voté']
            },
            {
                'name': 'Town Crier',
                'ability_description': "Chaque nuit*, vous apprenez si un Sbire a nominé aujourd'hui.",
                'first_night': None,
                'other_nights': 36,
                'remind_tokens': ['Sbire a nominé']
            },
            {
                'name': 'Oracle',
                'ability_description': "Chaque nuit*, vous apprenez combien de joueurs morts sont Maléfiques.",
                'first_night': None,
                'other_nights': 37,
                'remind_tokens': []
            },
            {
                'name': 'Savant',
                'ability_description': "Chaque jour, vous pouvez visiter le Conteur pour apprendre 2 choses en jeu, dont 1 vraie et 1 fausse.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Seamstress',
                'ability_description': "Une fois par partie, de nuit, choisissez 2 joueurs (ou vous deux fois) : vous apprenez s'ils sont du même alignement.",
                'first_night': 22,
                'other_nights': 38,
                'remind_tokens': ['Pas utilisé']
            },
            {
                'name': 'Philosopher',
                'ability_description': "Une fois par partie, la nuit, choisissez un personnage Bon : vous gagnez cette capacité. Si ce personnage est en jeu, il devient ivre.",
                'first_night': 1,
                'other_nights': 1,
                'remind_tokens': ['Ivre', 'Est le']
            },
            {
                'name': 'Artist',
                'ability_description': "Une fois par partie, de jour, posez au Conteur une question fermée : il répond honnêtement.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Pas utilisé']
            },
            {
                'name': 'Juggler',
                'ability_description': "Le jour 1, désignez publiquement 5 joueurs et 5 personnages : cette nuit, vous apprenez combien de suppositions étaient correctes.",
                'first_night': None,
                'other_nights': 39,
                'remind_tokens': []
            },
            {
                'name': 'Sage',
                'ability_description': "Si le Démon vous tue, vous apprenez qu'il est le Démon et qui sont les 2 joueurs vivants.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            }
        ]
        
        for char_data in townsfolk:
            character = Character(
                name=char_data['name'],
                edition_id=sects.id,
                character_type=Character.TOWNSFOLK,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Personnages OUTSIDER (Étrangers)
        print("🎭 Ajout des Étrangers...")
        outsiders = [
            {
                'name': 'Mutant',
                'ability_description': "Si vous êtes 'fou' que vous êtes un Étranger, vous pourriez être exécuté.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Sweetheart',
                'ability_description': "Quand vous mourez, 1 joueur est ivre à partir de maintenant.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Ivre']
            },
            {
                'name': 'Barber',
                'ability_description': "Si vous êtes mort : la nuit, le Démon choisit 2 joueurs (pas lui) qui échangent leurs personnages.",
                'first_night': None,
                'other_nights': 32,
                'remind_tokens': ['Échange']
            },
            {
                'name': 'Klutz',
                'ability_description': "Quand vous apprenez que vous êtes mort, désignez publiquement un joueur : s'il est Maléfique, votre équipe perd.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            }
        ]
        
        for char_data in outsiders:
            character = Character(
                name=char_data['name'],
                edition_id=sects.id,
                character_type=Character.OUTSIDER,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Personnages MINION (Sbires)
        print("😈 Ajout des Sbires...")
        minions = [
            {
                'name': 'Evil Twin',
                'ability_description': "Vous et un Villageois opposé savez qui vous êtes. Si le Bon jumeau est exécuté, le Mal gagne. Les Bons joueurs ne peuvent pas vous exécuter.",
                'first_night': 23,
                'other_nights': None,
                'remind_tokens': ['Jumeau']
            },
            {
                'name': 'Witch',
                'ability_description': "Chaque nuit, choisissez un joueur : s'il nomine demain, il meurt. Si 1 Bon joueur est exécuté, vous mourez.",
                'first_night': 16,
                'other_nights': 13,
                'remind_tokens': ['Maudit']
            },
            {
                'name': 'Cerenovus',
                'ability_description': "Chaque nuit, choisissez un joueur et un personnage : il est 'fou' qu'il est ce personnage demain, ou pourrait être exécuté.",
                'first_night': 17,
                'other_nights': 14,
                'remind_tokens': ['Fou']
            },
            {
                'name': 'Pit-Hag',
                'ability_description': "Chaque nuit*, choisissez un joueur et un personnage : si faisable, il devient ce personnage. Si créé, un Démon meurt.",
                'first_night': None,
                'other_nights': 12,
                'remind_tokens': []
            }
        ]
        
        for char_data in minions:
            character = Character(
                name=char_data['name'],
                edition_id=sects.id,
                character_type=Character.MINION,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Personnages DEMON (Démons)
        print("👹 Ajout des Démons...")
        demons = [
            {
                'name': 'Fang Gu',
                'ability_description': "Chaque nuit*, choisissez un joueur : il meurt. La première fois qu'un Étranger meurt ainsi, il devient le Fang Gu et vous devenez un Villageois.",
                'first_night': None,
                'other_nights': 17,
                'remind_tokens': ['Mort', 'Étranger est Fang Gu']
            },
            {
                'name': 'Vigormortis',
                'ability_description': "Chaque nuit*, choisissez un joueur : il meurt. Les Sbires que vous tuez gardent leur capacité et empoisonnent 1 Villageois voisin.",
                'first_night': None,
                'other_nights': 18,
                'remind_tokens': ['Mort', 'Empoisonné']
            },
            {
                'name': 'No Dashii',
                'ability_description': "Chaque nuit*, choisissez un joueur : il meurt. Vos 2 voisins Villageois vivants sont empoisonnés.",
                'first_night': None,
                'other_nights': 19,
                'remind_tokens': ['Mort', 'Empoisonné']
            },
            {
                'name': 'Vortox',
                'ability_description': "Chaque nuit*, choisissez un joueur : il meurt. Les capacités Villageois donnent de fausses informations. Chaque jour, si personne n'est exécuté, le Mal gagne.",
                'first_night': None,
                'other_nights': 20,
                'remind_tokens': ['Mort']
            }
        ]
        
        for char_data in demons:
            character = Character(
                name=char_data['name'],
                edition_id=sects.id,
                character_type=Character.DEMON,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Commit final
        db.session.commit()
        
        print("\n✅ Sects & Violets ajouté avec succès !")
        print(f"   - 13 Villageois")
        print(f"   - 4 Étrangers")
        print(f"   - 4 Sbires")
        print(f"   - 4 Démons")
        print(f"   Total : {Character.query.filter_by(edition_id=sects.id).count()} personnages\n")

if __name__ == '__main__':
    seed_sects_and_violets()

