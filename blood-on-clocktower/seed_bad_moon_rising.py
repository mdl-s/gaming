"""Script pour ajouter l'édition Bad Moon Rising."""
from app import create_app, db
from app.models import Edition, Character

def seed_bad_moon_rising():
    """Ajoute Bad Moon Rising et ses personnages."""
    
    app = create_app()
    
    with app.app_context():
        # Vérifier si l'édition existe déjà
        existing = Edition.query.filter_by(name="Bad Moon Rising").first()
        if existing:
            print("⚠️  Bad Moon Rising existe déjà !")
            return
        
        # Créer l'édition Bad Moon Rising
        print("📚 Création de l'édition Bad Moon Rising...")
        bad_moon = Edition(
            name="Bad Moon Rising",
            description="L'édition intermédiaire avec des morts multiples la nuit et des mécaniques de résurrection.",
            difficulty_level=2
        )
        db.session.add(bad_moon)
        db.session.commit()
        
        # Personnages TOWNSFOLK (Villageois)
        print("👥 Ajout des Villageois...")
        townsfolk = [
            {
                'name': 'Grandmother',
                'ability_description': "Vous commencez en connaissant un Bon joueur et son personnage. Si le Démon vous tue, il meurt aussi.",
                'first_night': 18,
                'other_nights': None,
                'remind_tokens': ['Grandchild']
            },
            {
                'name': 'Sailor',
                'ability_description': "Chaque nuit, choisissez un joueur vivant : soit vous, soit lui est ivre jusqu'au crépuscule. Vous ne pouvez pas mourir.",
                'first_night': 3,
                'other_nights': 2,
                'remind_tokens': ['Ivre']
            },
            {
                'name': 'Chambermaid',
                'ability_description': "Chaque nuit, choisissez 2 joueurs vivants (pas vous) : vous apprenez combien se sont réveillés cette nuit à cause de leur capacité.",
                'first_night': None,
                'other_nights': 35,
                'remind_tokens': []
            },
            {
                'name': 'Exorcist',
                'ability_description': "Chaque nuit*, choisissez un joueur (pas vous) : le Démon, s'il choisit cette nuit, ne tue pas.",
                'first_night': None,
                'other_nights': 11,
                'remind_tokens': ['Choisi']
            },
            {
                'name': 'Innkeeper',
                'ability_description': "Chaque nuit*, choisissez 2 joueurs : ils ne peuvent pas mourir cette nuit, mais l'un est ivre jusqu'au crépuscule.",
                'first_night': None,
                'other_nights': 3,
                'remind_tokens': ['Protégé', 'Ivre']
            },
            {
                'name': 'Gambler',
                'ability_description': "Chaque nuit*, choisissez un joueur et devinez son personnage : si vous avez tort, vous mourez.",
                'first_night': None,
                'other_nights': 6,
                'remind_tokens': ['Mort']
            },
            {
                'name': 'Gossip',
                'ability_description': "Chaque jour, vous pouvez faire une déclaration publique. Cette nuit, si c'était vrai, un joueur meurt.",
                'first_night': None,
                'other_nights': 25,
                'remind_tokens': ['Mort']
            },
            {
                'name': 'Courtier',
                'ability_description': "Chaque nuit, choisissez 2 joueurs (pas vous) : demain, ils ne peuvent pas nominer.",
                'first_night': None,
                'other_nights': 7,
                'remind_tokens': ['Pas de nomination']
            },
            {
                'name': 'Professor',
                'ability_description': "Une fois par partie, la nuit*, choisissez un joueur mort : s'il est un Villageois, il est ressuscité.",
                'first_night': None,
                'other_nights': 30,
                'remind_tokens': ['Ressuscité', 'Pas utilisé']
            },
            {
                'name': 'Minstrel',
                'ability_description': "Quand un Sbire meurt par exécution, tous les autres joueurs (pas vous) sont ivres jusqu'au crépuscule demain.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Tous ivres']
            },
            {
                'name': 'Tea Lady',
                'ability_description': "Si vos deux voisins vivants sont Bons, ils ne peuvent pas mourir.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Pacifist',
                'ability_description': "Les Bons joueurs exécutés peuvent choisir de ne pas mourir.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Fool',
                'ability_description': "La première fois que vous mourez, vous ne mourez pas vraiment. [Le Conteur vous dit quand]",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Pas utilisé']
            }
        ]
        
        for char_data in townsfolk:
            character = Character(
                name=char_data['name'],
                edition_id=bad_moon.id,
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
                'name': 'Tinker',
                'ability_description': "Vous pouvez mourir à tout moment.",
                'first_night': None,
                'other_nights': 29,
                'remind_tokens': []
            },
            {
                'name': 'Moonchild',
                'ability_description': "Quand vous apprenez que vous êtes mort, désignez publiquement un joueur : s'il est Bon, il meurt cette nuit.",
                'first_night': None,
                'other_nights': 28,
                'remind_tokens': ['Mort']
            },
            {
                'name': 'Goon',
                'ability_description': "Chaque nuit, la première fois que vous vous réveillez, choisissez un joueur (pas vous) : il est ivre jusqu'au crépuscule. Vous commencez en connaissant 1 Sbire.",
                'first_night': 17,
                'other_nights': 27,
                'remind_tokens': ['Ivre']
            },
            {
                'name': 'Lunatic',
                'ability_description': "Vous pensez être un Démon, mais vous ne l'êtes pas. Le Démon sait qui vous êtes et qui vous choisissez la nuit.",
                'first_night': None,
                'other_nights': None,
                'setup_info': "Le Lunatic pense être le Démon et reçoit de fausses informations.",
                'remind_tokens': []
            }
        ]
        
        for char_data in outsiders:
            character = Character(
                name=char_data['name'],
                edition_id=bad_moon.id,
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
                'name': 'Godfather',
                'ability_description': "Vous commencez en connaissant quels Étrangers sont en jeu. Si 1 meurt durant le jour, un autre joueur peut mourir cette nuit.",
                'first_night': 19,
                'other_nights': 26,
                'remind_tokens': ['Mort']
            },
            {
                'name': 'Devil\'s Advocate',
                'ability_description': "Chaque nuit, choisissez un joueur vivant (pas vous) : si exécuté demain, il ne meurt pas.",
                'first_night': 8,
                'other_nights': 5,
                'remind_tokens': ['Protégé']
            },
            {
                'name': 'Assassin',
                'ability_description': "Une fois par partie, la nuit*, choisissez un joueur : il meurt, même si protégé.",
                'first_night': None,
                'other_nights': 22,
                'remind_tokens': ['Mort', 'Pas utilisé']
            },
            {
                'name': 'Mastermind',
                'ability_description': "Si le Démon meurt par exécution (vivant ou mort), jouez 1 jour de plus. Si un joueur est alors exécuté, son équipe perd.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            }
        ]
        
        for char_data in minions:
            character = Character(
                name=char_data['name'],
                edition_id=bad_moon.id,
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
                'name': 'Zombuul',
                'ability_description': "Chaque nuit*, si personne n'est mort aujourd'hui, choisissez un joueur : il meurt. La première fois que vous mourriez, vous vivez mais enregistrez une mort.",
                'first_night': None,
                'other_nights': 21,
                'remind_tokens': ['Mort', 'Mort enregistrée']
            },
            {
                'name': 'Pukka',
                'ability_description': "Chaque nuit, choisissez un joueur : il est empoisonné. La nuit suivante, il meurt puis un nouveau joueur est empoisonné.",
                'first_night': 14,
                'other_nights': 18,
                'remind_tokens': ['Empoisonné', 'Meurt']
            },
            {
                'name': 'Shabaloth',
                'ability_description': "Chaque nuit*, choisissez 2 joueurs : ils meurent. Un joueur mort que vous choisissez peut être ressuscité pour mourir à nouveau.",
                'first_night': None,
                'other_nights': 19,
                'remind_tokens': ['Mort', 'Vivant']
            },
            {
                'name': 'Po',
                'ability_description': "Chaque nuit*, vous pouvez choisir un joueur : il meurt. Si votre dernière sélection était personne, choisissez 3 joueurs cette nuit.",
                'first_night': None,
                'other_nights': 20,
                'remind_tokens': ['Mort', '3 attaques']
            }
        ]
        
        for char_data in demons:
            character = Character(
                name=char_data['name'],
                edition_id=bad_moon.id,
                character_type=Character.DEMON,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        # Commit final
        db.session.commit()
        
        print("\n✅ Bad Moon Rising ajouté avec succès !")
        print(f"   - 13 Villageois")
        print(f"   - 4 Étrangers")
        print(f"   - 4 Sbires")
        print(f"   - 4 Démons")
        print(f"   Total : {Character.query.filter_by(edition_id=bad_moon.id).count()} personnages\n")

if __name__ == '__main__':
    seed_bad_moon_rising()

