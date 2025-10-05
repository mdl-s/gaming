"""Script master pour peupler toutes les éditions."""
import sys
from seed_data import seed_database
from seed_bad_moon_rising import seed_bad_moon_rising
from seed_sects_and_violets import seed_sects_and_violets
from seed_travellers import seed_travellers

def seed_all():
    """Peuple la base avec toutes les éditions disponibles."""
    
    print("=" * 60)
    print("🕐 BLOOD ON THE CLOCKTOWER - SEED COMPLET")
    print("=" * 60)
    print()
    
    # Trouble Brewing (inclus dans seed_database)
    print("📦 Étape 1/4 : Trouble Brewing")
    print("-" * 60)
    try:
        seed_database()
    except Exception as e:
        print(f"❌ Erreur Trouble Brewing : {e}")
        print("   (Peut-être déjà peuplé, on continue...)")
    print()
    
    # Bad Moon Rising
    print("📦 Étape 2/4 : Bad Moon Rising")
    print("-" * 60)
    try:
        seed_bad_moon_rising()
    except Exception as e:
        print(f"❌ Erreur Bad Moon Rising : {e}")
    print()
    
    # Sects & Violets
    print("📦 Étape 3/4 : Sects & Violets")
    print("-" * 60)
    try:
        seed_sects_and_violets()
    except Exception as e:
        print(f"❌ Erreur Sects & Violets : {e}")
    print()
    
    # Travellers
    print("📦 Étape 4/4 : Travellers")
    print("-" * 60)
    try:
        seed_travellers()
    except Exception as e:
        print(f"❌ Erreur Travellers : {e}")
    print()
    
    print("=" * 60)
    print("✅ SEED COMPLET TERMINÉ !")
    print("=" * 60)
    print()
    print("📊 Résumé :")
    print("   - Trouble Brewing : 22 personnages")
    print("   - Bad Moon Rising : 25 personnages")
    print("   - Sects & Violets : 25 personnages")
    print("   - Travellers : 15 personnages")
    print("   TOTAL : ~87 personnages")
    print()
    print("🎮 L'application est prête avec 3 éditions + Travellers !")
    print()

if __name__ == '__main__':
    seed_all()

