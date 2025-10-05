"""Point d'entrée pour lancer l'application Flask."""
import os
from app import create_app, db
from app.models import Edition, Character, Game, Player, NightAction, DayAction, ReminderToken

# Créer l'application
app = create_app(os.getenv('FLASK_ENV', 'development'))

# Contexte du shell pour faciliter le débogage
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Edition': Edition,
        'Character': Character,
        'Game': Game,
        'Player': Player,
        'NightAction': NightAction,
        'DayAction': DayAction,
        'ReminderToken': ReminderToken
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

