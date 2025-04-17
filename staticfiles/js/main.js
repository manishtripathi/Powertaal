// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const closeButton = alert.querySelector('.btn-close');
            if (closeButton) {
                closeButton.click();
            }
        }, 5000);
    });

    // Add active class to current nav link
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(function(link) {
        const href = link.getAttribute('href');
        if (href === currentLocation || currentLocation.startsWith(href) && href !== '/') {
            link.classList.add('active');
        }
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Language selector
    const languageSelect = document.querySelector('.language-select');
    if (languageSelect) {
        languageSelect.addEventListener('change', function() {
            // Here you would typically submit a form or make an AJAX request
            // For now, we'll just log the selected language
            console.log('Selected language:', this.value);
        });
    }

    // Password strength meter
    const passwordInput = document.getElementById('id_password1');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            let strength = 0;
            
            // Check password length
            if (password.length >= 8) {
                strength += 1;
            }
            
            // Check for mixed case
            if (password.match(/[a-z]/) && password.match(/[A-Z]/)) {
                strength += 1;
            }
            
            // Check for numbers
            if (password.match(/\d/)) {
                strength += 1;
            }
            
            // Check for special characters
            if (password.match(/[^a-zA-Z\d]/)) {
                strength += 1;
            }
            
            // Update UI based on strength
            const strengthMeter = document.createElement('div');
            strengthMeter.className = 'progress mt-2';
            strengthMeter.innerHTML = `
                <div class="progress-bar ${getStrengthClass(strength)}" 
                     role="progressbar" 
                     style="width: ${strength * 25}%" 
                     aria-valuenow="${strength}" 
                     aria-valuemin="0" 
                     aria-valuemax="4">
                    ${getStrengthText(strength)}
                </div>
            `;
            
            // Remove any existing strength meter
            const existingMeter = this.parentNode.querySelector('.progress');
            if (existingMeter) {
                existingMeter.remove();
            }
            
            // Add the new strength meter
            this.parentNode.appendChild(strengthMeter);
        });
    }

    // Helper functions for password strength
    function getStrengthClass(strength) {
        switch (strength) {
            case 0:
                return 'bg-danger';
            case 1:
                return 'bg-warning';
            case 2:
                return 'bg-info';
            case 3:
                return 'bg-primary';
            case 4:
                return 'bg-success';
            default:
                return 'bg-secondary';
        }
    }

    function getStrengthText(strength) {
        switch (strength) {
            case 0:
                return 'Zeer zwak';
            case 1:
                return 'Zwak';
            case 2:
                return 'Gemiddeld';
            case 3:
                return 'Sterk';
            case 4:
                return 'Zeer sterk';
            default:
                return '';
        }
    }
}); 