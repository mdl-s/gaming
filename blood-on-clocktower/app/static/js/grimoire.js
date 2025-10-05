// JavaScript pour l'interface Grimoire

// Raccourcis clavier
document.addEventListener('keydown', function(event) {
    // Échap pour fermer les modals
    if (event.key === 'Escape') {
        closeAllModals();
    }
});

function closeAllModals() {
    const modals = document.querySelectorAll('[id$="Modal"]');
    modals.forEach(modal => {
        modal.classList.add('hidden');
    });
}

// Confirmation avant actions critiques
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// Toast notifications
function showToast(message, type = 'info') {
    const colors = {
        'info': 'bg-blue-600',
        'success': 'bg-green-600',
        'error': 'bg-red-600',
        'warning': 'bg-yellow-600'
    };
    
    const toast = document.createElement('div');
    toast.className = `fixed top-20 right-4 z-50 px-6 py-3 rounded-lg shadow-lg text-white ${colors[type]} animate-slideIn`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.transition = 'opacity 0.5s';
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}

// Drag and drop pour réorganiser les joueurs (futur)
function enableDragDrop() {
    // TODO: Implémenter le drag & drop
    console.log('Drag & drop à implémenter');
}

// Auto-save des notes
let notesTimeout;
function autoSaveNotes(playerId, gameId) {
    clearTimeout(notesTimeout);
    notesTimeout = setTimeout(() => {
        const notes = document.getElementById('player-notes').value;
        
        fetch(`/grimoire/${gameId}/player/${playerId}/notes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ notes: notes })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showToast('Notes sauvegardées', 'success');
            }
        })
        .catch(error => {
            console.error('Erreur:', error);
        });
    }, 2000); // Sauvegarde après 2 secondes d'inactivité
}

// Initialisation
document.addEventListener('DOMContentLoaded', function() {
    // Réinitialiser les icônes Lucide après chargement dynamique
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    console.log('Blood on the Clocktower - Grimoire chargé');
});

