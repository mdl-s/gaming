"""Script pour ajouter les Travellers (personnages itinérants)."""
from app import create_app, db
from app.models import Edition, Character

def seed_travellers():
    """Ajoute les Travellers pour toutes les éditions."""
    
    app = create_app()
    
    with app.app_context():
        # Les Travellers ne sont pas liés à une édition spécifique
        # On va créer une "édition" virtuelle pour eux
        travellers_edition = Edition.query.filter_by(name="Travellers").first()
        if not travellers_edition:
            print("📚 Création de l'édition Travellers...")
            travellers_edition = Edition(
                name="Travellers",
                description="Personnages itinérants pouvant être ajoutés ou retirés en cours de partie.",
                difficulty_level=2,
                is_active=False  # Pas sélectionnable comme édition principale
            )
            db.session.add(travellers_edition)
            db.session.commit()
        
        # Vérifier si les Travellers existent déjà
        existing_count = Character.query.filter_by(
            edition_id=travellers_edition.id,
            character_type=Character.TRAVELLER
        ).count()
        
        if existing_count > 0:
            print(f"⚠️  {existing_count} Travellers existent déjà !")
            return
        
        print("🧳 Ajout des Travellers...")
        
        travellers = [
            # Trouble Brewing Travellers
            {
                'name': 'Scapegoat',
                'ability_description': "Si un joueur d'un même alignement est exécuté, vous pourriez être exécuté à la place.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Gunslinger',
                'ability_description': "Chaque jour, après la première nomination, vous pouvez publiquement choisir un joueur : s'il est en vie ce soir, il meurt.",
                'first_night': None,
                'other_nights': 31,
                'remind_tokens': []
            },
            {
                'name': 'Beggar',
                'ability_description': "Vous devez demander à un joueur de voter pour vous. Si un joueur Maléfique vote pour vous, votre équipe perd.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Bureaucrat',
                'ability_description': "Chaque nuit, choisissez un joueur (pas vous) : son vote compte comme 3 votes demain.",
                'first_night': 9,
                'other_nights': 8,
                'remind_tokens': ['x3 votes']
            },
            {
                'name': 'Thief',
                'ability_description': "Chaque nuit, choisissez un joueur (pas vous) : leurs votes comptent négativement demain.",
                'first_night': 10,
                'other_nights': 9,
                'remind_tokens': ['Votes négatifs']
            },
            
            # Bad Moon Rising Travellers
            {
                'name': 'Apprentice',
                'ability_description': "La première nuit, vous gagnez une capacité de Villageois (ne jouant pas).",
                'first_night': 2,
                'other_nights': None,
                'remind_tokens': ['Capacité', 'Est le']
            },
            {
                'name': 'Matron',
                'ability_description': "Chaque jour, vous pouvez choisir jusqu'à 3 paires de joueurs pour échanger leurs sièges. Les joueurs ne peuvent nominer qu'après avoir échangé de siège.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Judge',
                'ability_description': "Une fois par partie, si une exécution est sur le point d'avoir lieu, vous pouvez l'annuler. Si vous le faites, vous ne pouvez pas nominer pour le reste de la partie.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Pas utilisé', 'Pas de nomination']
            },
            {
                'name': 'Bishop',
                'ability_description': "Seulement les Villageois peuvent nominer. Avec 5+ joueurs vivants, 1 joueur peut être exilé aujourd'hui : ils ne peuvent plus être nominés ou voter.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': ['Exilé']
            },
            {
                'name': 'Voudon',
                'ability_description': "Seulement les Étrangers peuvent nominer. Chaque jour, si personne n'est exécuté, un joueur vivant meurt cette nuit.",
                'first_night': None,
                'other_nights': 24,
                'remind_tokens': ['Mort']
            },
            
            # Sects & Violets Travellers
            {
                'name': 'Barista',
                'ability_description': "Chaque nuit, jusqu'au crépuscule : 1) un joueur devient sobre, sain et obtient de vraies informations ; 2) un joueur agit deux fois.",
                'first_night': 4,
                'other_nights': 2,
                'remind_tokens': ['Sobre et sain', 'Agit 2x']
            },
            {
                'name': 'Harlot',
                'ability_description': "Chaque nuit*, choisissez un joueur vivant : si c'est le Démon, ils meurent.",
                'first_night': None,
                'other_nights': 16,
                'remind_tokens': []
            },
            {
                'name': 'Butcher',
                'ability_description': "Chaque jour, après la première exécution, vous pouvez nominer à nouveau.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            },
            {
                'name': 'Bone Collector',
                'ability_description': "Une fois par partie, la nuit, choisissez un joueur mort : il récupère sa capacité jusqu'au crépuscule.",
                'first_night': None,
                'other_nights': 31,
                'remind_tokens': ['Pas utilisé', 'Capacité']
            },
            {
                'name': 'Deviant',
                'ability_description': "Si vous étiez fou que vous étiez Bon : les joueurs Bons que vous choisissez pourraient enregistrer comme Maléfiques & vice versa.",
                'first_night': None,
                'other_nights': None,
                'remind_tokens': []
            }
        ]
        
        for char_data in travellers:
            character = Character(
                name=char_data['name'],
                edition_id=travellers_edition.id,
                character_type=Character.TRAVELLER,
                ability_description=char_data['ability_description'],
                first_night=char_data.get('first_night'),
                other_nights=char_data.get('other_nights'),
                remind_tokens=char_data.get('remind_tokens', [])
            )
            db.session.add(character)
        
        db.session.commit()
        
        print(f"\n✅ {len(travellers)} Travellers ajoutés avec succès !\n")

if __name__ == '__main__':
    seed_travellers()

