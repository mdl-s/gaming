"""Script pour peupler la base de données avec les données de Trouble Brewing."""
from app import create_app, db
from app.models import Edition, Character

def seed_database():
    """Peuple la base de données avec l'édition Trouble Brewing et ses personnages."""
    
    app = create_app()
    
    with app.app_context():
        # Supprimer toutes les données existantes
        print("🗑️  Nettoyage de la base de données...")
        db.drop_all()
        db.create_all()
        
        # Créer l'édition Trouble Brewing
        print("📚 Création de l'édition Trouble Brewing...")
        trouble_brewing = Edition(
            name="Trouble Brewing",
            description="L'édition de base, parfaite pour les débutants. Un démon, des sbires, et un village qui doit démasquer le Mal.",
            difficulty_level=1
        )
        db.session.add(trouble_brewing)
        db.session.commit()
        
        # Personnages TOWNSFOLK (Villageois)
        print("👥 Ajout des Villageois...")
        townsfolk = [
            {
                'name': 'Washerwoman',
                'ability_description': "Vous commencez en sachant qu'un Villageois spécifique est en jeu (entre 2 joueurs).",
                'first_night': 11,
                'other_nights': None,
                'remind_tokens': ['Villageois', 'Fausse info']
            },
            {
                'name': 'Librarian',
                'ability_description': "Vous commencez en sachant qu'un Étranger spécifique est en jeu (entre 2 joueurs).",
                'first_night': 12,
                'other_nights': None,
                'remind_tokens': ['Étranger', 'Fausse info']
            },
            {
                'name': 'Investigator',
                'ability_description': "Vous commencez en sachant qu'un Sbire spécifique est en jeu (entre 2 joueurs).",
                'first_night': 13,
                'other_nights': None,
                'remind_tokens': ['Sbire', 'Fausse info']
            },
            {
                'name': 'Chef',
                'ability_description': "Vous commencez en sachant combien de paires de joueurs maléfiques sont assises adjacentes.",
                'first_night': 14,
                'other_nights': None,
                'remind_tokens': ['Paire']
            },
            {
                'name': 'Empath',
                'ability_description': "Chaque nuit, vous apprenez combien de vos voisins vivants sont maléfiques.",
                'first_night': 15,
                'other_nights': 26,
                'remind_tokens': ['Maléfique']
            },
            {
                'name': 'Fortune Teller',
                'ability_description': "Chaque nuit, choisissez 2 joueurs : vous apprenez si l'un d'eux est le Démon. Il y a un Faux Positif.",
                'first_night': 16,
                'other_nights': 27,
                'remind_tokens': ['Faux Positif']
            },
            {
                'name': 'Undertaker',
                'ability_description': "Chaque nuit*, vous apprenez quel personnage a été exécuté aujourd'hui.",
                'first_night': None,
                'other_nights': 32,
                'remind_tokens': ['Exécuté']
            },
            {
                'name': 'Monk',
                'ability_description': "Chaque nuit*, choisissez un joueur (pas vous) : il est protégé du Démon cette nuit.",
                'first_night': None,
                'other_nights': 7,
                'remind_tokens': ['Protégé']
            },
            {
                'name': 'Ravenkeeper',
                'ability_description': "Si vous mourez la nuit, vous êtes réveillé et choisissez un joueur : vous apprenez son personnage.",
                'first_night': None,
                'other_nights': 31,
                'remind_tokens': []
            },
            {
                'name': 'Virgin',
                'ability_description': "La première fois que vous êtes nominé, si le nominateur est un Villageois, il est exécuté immédiatement.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Pas utilisé']
            },
            {
                'name': 'Slayer',
                'ability_description': "Une fois par partie, pendant le jour, déclarez publiquement que vous utilisez cette capacité pour tuer un joueur : s'il est le Démon, il meurt.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Pas utilisé']
            },
            {
                'name': 'Soldier',
                'ability_description': "Vous êtes protégé du Démon.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Mayor',
                'ability_description': "S'il ne reste que 3 joueurs en vie et qu'aucune exécution n'a lieu, votre équipe gagne. Si vous mourez la nuit, un autre joueur peut mourir à la place.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            }
        ]
        
        for char_data in townsfolk:
            character = Character(
                name=char_data['name'],
                edition_id=trouble_brewing.id,
                character_type=Character.TOWNSFOLK,
                ability_description=char_data['ability_description'],
                first_night=char_data['first_night'],
                other_nights=char_data['other_nights'],
                remind_tokens=char_data['remind_tokens']
            )
            db.session.add(character)
        
        # Personnages OUTSIDER (Étrangers)
        print("🎭 Ajout des Étrangers...")
        outsiders = [
            {
                'name': 'Drunk',
                'ability_description': "Vous ne savez pas que vous êtes le Drunk. Vous pensez être un Villageois, mais vous n'êtes pas ce personnage.",
                'first_night': None,
                'other_nights': None,
                'setup_info': "Le Drunk pense avoir un rôle de Villageois qu'il n'a pas.",
                'remind_tokens': ['Ivre']
            },
            {
                'name': 'Recluse',
                'ability_description': "Vous pouvez apparaître comme maléfique ou comme un Sbire/Démon aux capacités qui vous ciblent, même si vous êtes bon.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Faux Maléfique']
            },
            {
                'name': 'Saint',
                'ability_description': "Si vous êtes exécuté, votre équipe perd.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Butler',
                'ability_description': "Chaque nuit, choisissez un joueur (pas vous) : demain, vous ne pouvez voter que s'il vote.",
                'first_night': 17,
                'other_nights': 28,
                'remind_tokens': ['Maître']
            }
        ]
        
        for char_data in outsiders:
            character = Character(
                name=char_data['name'],
                edition_id=trouble_brewing.id,
                character_type=Character.OUTSIDER,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                setup_info=char_data.get('setup_info'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Personnages MINION (Sbires)
        print("😈 Ajout des Sbires...")
        minions = [
            {
                'name': 'Poisoner',
                'ability_description': "Chaque nuit, choisissez un joueur : il est empoisonné cette nuit et le jour suivant.",
                'first_night': 6,
                'other_nights': 4,
                'remind_tokens': ['Empoisonné']
            },
            {
                'name': 'Spy',
                'ability_description': "Chaque nuit, vous voyez le Grimoire. Vous pouvez apparaître comme bon, comme Villageois/Étranger, ou comme un personnage différent.",
                'first_night': 25,
                'other_nights': 42,
                'remind_tokens': []
            },
            {
                'name': 'Scarlet Woman',
                'ability_description': "Si 5 joueurs ou plus sont en vie et que le Démon meurt, vous devenez le Démon.",
                'first_night': None,
                'other_nights': 12,
                'remind_tokens': ['Scarlet Woman']
            },
            {
                'name': 'Baron',
                'ability_description': "Il y a 2 Étrangers supplémentaires en jeu. [+2 Étrangers]",
                'first_night': None,
                'other_nights': None,
                'setup_info': "Remplacer 2 Villageois par 2 Étrangers supplémentaires.",
                'remind_tokens': []
            }
        ]
        
        for char_data in minions:
            character = Character(
                name=char_data['name'],
                edition_id=trouble_brewing.id,
                character_type=Character.MINION,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                setup_info=char_data.get('setup_info'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Personnage DEMON (Démon)
        print("👹 Ajout du Démon...")
        demons = [
            {
                'name': 'Imp',
                'ability_description': "Chaque nuit*, choisissez un joueur : il meurt. Si vous vous tuez, un Sbire devient l'Imp.",
                'first_night': None,
                'other_nights': 15,
                'remind_tokens': ['Mort']
            }
        ]
        
        for char_data in demons:
            character = Character(
                name=char_data['name'],
                edition_id=trouble_brewing.id,
                character_type=Character.DEMON,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Commit final
        db.session.commit()
        
        print("\n✅ Base de données peuplée avec succès !")
        print(f"   - 1 édition créée")
        print(f"   - 13 Villageois")
        print(f"   - 4 Étrangers")
        print(f"   - 4 Sbires")
        print(f"   - 1 Démon")
        print(f"   Total : {Character.query.count()} personnages\n")

if __name__ == '__main__':
    seed_database()

