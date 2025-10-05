// JavaScript principal pour l'application

// Utilitaires
const utils = {
    // Formater une date
    formatDate: function(dateString) {
        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        return new Date(dateString).toLocaleDateString('fr-FR', options);
    },
    
    // Copier dans le presse-papier
    copyToClipboard: function(text) {
        navigator.clipboard.writeText(text).then(() => {
            this.showNotification('Copié dans le presse-papier !', 'success');
        });
    },
    
    // Afficher une notification
    showNotification: function(message, type = 'info') {
        const colors = {
            'info': 'bg-blue-600',
            'success': 'bg-green-600',
            'error': 'bg-red-600',
            'warning': 'bg-yellow-600'
        };
        
        const notification = document.createElement('div');
        notification.className = `fixed top-20 right-4 z-50 px-6 py-3 rounded-lg shadow-lg text-white ${colors[type]}`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.transition = 'opacity 0.5s';
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 500);
        }, 3000);
    }
};

// Confirmation avant suppression
function confirmDelete(event, itemName = 'cet élément') {
    if (!confirm(`Êtes-vous sûr de vouloir supprimer ${itemName} ?`)) {
        event.preventDefault();
        return false;
    }
    return true;
}

// Initialisation
document.addEventListener('DOMContentLoaded', function() {
    // Initialiser les icônes Lucide
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    // Ajouter des confirmations sur les formulaires de suppression
    document.querySelectorAll('form[action*="delete"]').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('Confirmer la suppression ?')) {
                e.preventDefault();
            }
        });
    });
    
    // Auto-hide les messages flash après 5 secondes
    setTimeout(() => {
        document.querySelectorAll('.flash-message').forEach(msg => {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 500);
        });
    }, 5000);
    
    console.log('Blood on the Clocktower - Application chargée');
});

// Export des utilitaires pour utilisation globale
window.botcUtils = utils;

