/**
 * PowerTaal Logo Animation
 * Een subtiele maar elegante animatie voor het PowerTaal logo
 */

document.addEventListener('DOMContentLoaded', function() {
    // Zoek het logo-element
    const logo = document.querySelector('.brand-logo');
    const logoContainer = logo.parentElement;
    const tagline = document.querySelector('.tagline');
    
    // Alleen doorgaan als we het logo hebben gevonden
    if (!logo) {
        console.warn('PowerTaal Logo Animation: Logo element niet gevonden');
        return;
    }
    
    // Maak een wrapper voor het logo om de animatie te bevatten
    const wrapper = document.createElement('div');
    wrapper.className = 'logo-animation-wrapper';
    
    // Wrap het logo
    logoContainer.insertBefore(wrapper, logo);
    wrapper.appendChild(logo);
    
    // Animatie effect toevoegen (glow effect)
    addGlowEffect(logo);
    
    // Interactie effecten toevoegen
    addInteractionEffects(wrapper, logo, tagline);
    
    // Voeg periodieke animaties toe die automatisch afspelen
    startPeriodicAnimations(logo);
});

/**
 * Voegt een subtiel glow effect toe aan het logo
 */
function addGlowEffect(logo) {
    // Creëer een glow container
    const glowContainer = document.createElement('div');
    glowContainer.className = 'logo-glow-container';
    logo.parentElement.insertBefore(glowContainer, logo);
    glowContainer.appendChild(logo);
    
    // Creëer de glow elementen
    for (let i = 0; i < 3; i++) {
        const glowElement = document.createElement('div');
        glowElement.className = 'logo-glow-element';
        glowElement.style.opacity = 0.1 - (i * 0.03);
        glowElement.style.animationDelay = `${i * 0.5}s`;
        glowContainer.appendChild(glowElement);
    }
}

/**
 * Voegt interactie effecten toe wanneer de gebruiker over het logo beweegt
 */
function addInteractionEffects(wrapper, logo, tagline) {
    // Hover effect
    wrapper.addEventListener('mouseenter', function() {
        logo.classList.add('logo-hover');
        wrapper.classList.add('active');
    });
    
    wrapper.addEventListener('mouseleave', function() {
        logo.classList.remove('logo-hover');
        wrapper.classList.remove('active');
    });
    
    // Klik effect
    wrapper.addEventListener('click', function() {
        playClickAnimation(logo);
    });
    
    // Voeg een subtiel zwevingseffect toe
    addFloatingEffect(logo);
    
    // Voeg tagline animatie toe
    addTaglineAnimation(tagline);
}

/**
 * Voegt een klik animatie toe
 */
function playClickAnimation(logo) {
    logo.classList.add('logo-click');
    
    // Maak een paar deeltjes voor een leuk effect
    createParticles(logo);
    
    // Verwijder de animatieklasse na voltooiing
    setTimeout(() => {
        logo.classList.remove('logo-click');
    }, 500);
}

/**
 * Creëert deeltjes voor een leuk klikeffect
 */
function createParticles(logo) {
    const container = logo.parentElement;
    const colors = ['#FF6600', '#00b0f0', '#3d5a73', '#ffffff'];
    
    // Creëer 15 deeltjes
    for (let i = 0; i < 15; i++) {
        const particle = document.createElement('div');
        particle.className = 'logo-particle';
        
        // Willekeurige eigenschappen
        const size = Math.random() * 8 + 4;
        const color = colors[Math.floor(Math.random() * colors.length)];
        const left = 40 + (Math.random() * 20 - 10); // gecentreerd rond het logo
        const top = 40 + (Math.random() * 20 - 10);
        const angle = Math.random() * 360; // willekeurige richting
        const distance = 30 + Math.random() * 40; // willekeurige afstand
        
        // Stel eigenschappen in
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.backgroundColor = color;
        particle.style.left = `${left}%`;
        particle.style.top = `${top}%`;
        
        // Voeg toe aan DOM
        container.appendChild(particle);
        
        // Animeer het deeltje
        setTimeout(() => {
            particle.style.transform = `translate(${Math.cos(angle) * distance}px, ${Math.sin(angle) * distance}px)`;
            particle.style.opacity = 0;
        }, 10);
        
        // Verwijder na animatie
        setTimeout(() => {
            container.removeChild(particle);
        }, 1000);
    }
}

/**
 * Voegt een subtiel zweef effect toe
 */
function addFloatingEffect(logo) {
    logo.classList.add('logo-floating');
}

/**
 * Start periodieke animaties die het logo leven geven
 */
function startPeriodicAnimations(logo) {
    // Elke 10 seconden een subtiele pulsatie tonen
    setInterval(() => {
        playPulseAnimation(logo);
    }, 10000);
    
    // Een initiele pulsatie om de aandacht te trekken
    setTimeout(() => {
        playPulseAnimation(logo);
    }, 2000);
}

/**
 * Speelt een subtiele pulsatie-animatie af op het logo
 */
function playPulseAnimation(logo) {
    logo.classList.add('logo-pulse');
    
    setTimeout(() => {
        logo.classList.remove('logo-pulse');
    }, 1000);
}

/**
 * Voegt tagline animatie toe
 */
function addTaglineAnimation(tagline) {
    if (!tagline) return;
    
    // Voeg een class toe voor styling
    tagline.classList.add('animated-tagline');
    
    // Subtiele animatie toevoegen voor de letters
    const text = tagline.textContent;
    tagline.textContent = '';
    
    // Voeg elke letter afzonderlijk toe met een kleine vertraging
    for (let i = 0; i < text.length; i++) {
        const charSpan = document.createElement('span');
        charSpan.className = 'tagline-char';
        charSpan.textContent = text[i];
        charSpan.style.animationDelay = `${i * 0.05}s`;
        tagline.appendChild(charSpan);
    }
}

// Voeg de benodigde CSS stijlen toe
(function addStyles() {
    const style = document.createElement('style');
    style.textContent = `
        /* Logo animatie basis stijlen */
        .logo-animation-wrapper {
            position: relative;
            display: inline-block;
            cursor: pointer;
            z-index: 10;
        }
        
        .logo-glow-container {
            position: relative;
            display: inline-block;
        }
        
        .logo-glow-element {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 10px;
            background: radial-gradient(ellipse at center, rgba(255, 102, 0, 0.4) 0%, rgba(255, 102, 0, 0) 70%);
            pointer-events: none;
            animation: logo-glow 3s ease-in-out infinite alternate;
            z-index: -1;
        }
        
        /* Zweef animatie */
        .logo-floating {
            animation: logo-float 6s ease-in-out infinite;
        }
        
        /* Hover effect */
        .logo-hover {
            transform: scale(1.05);
            filter: drop-shadow(0 5px 15px rgba(255, 102, 0, 0.4));
        }
        
        .logo-animation-wrapper.active .logo-glow-element {
            opacity: 0.3;
            animation: logo-glow-fast 1.5s ease-in-out infinite alternate;
        }
        
        /* Pulseer animatie */
        .logo-pulse {
            animation: logo-pulse 1s cubic-bezier(0.455, 0.03, 0.515, 0.955) forwards;
        }
        
        /* Klik animatie */
        .logo-click {
            transform: scale(0.95);
            transition: transform 0.2s ease;
        }
        
        /* Particle styling */
        .logo-particle {
            position: absolute;
            border-radius: 50%;
            pointer-events: none;
            transition: all 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
            z-index: 9;
        }
        
        /* Tagline animatie stijlen */
        .animated-tagline {
            display: inline-block;
            transition: all 0.3s ease;
        }
        
        .tagline-char {
            display: inline-block;
            animation: tagline-wave 2s ease-in-out infinite;
            animation-play-state: paused;
        }
        
        .logo-animation-wrapper:hover ~ .animated-tagline .tagline-char {
            animation-play-state: running;
        }
        
        /* Animaties */
        @keyframes logo-float {
            0% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-7px);
            }
            100% {
                transform: translateY(0);
            }
        }
        
        @keyframes logo-glow {
            0% {
                opacity: 0.1;
                transform: scale(1);
            }
            100% {
                opacity: 0.2;
                transform: scale(1.1);
            }
        }
        
        @keyframes logo-glow-fast {
            0% {
                opacity: 0.2;
                transform: scale(1);
            }
            100% {
                opacity: 0.4;
                transform: scale(1.15);
            }
        }
        
        @keyframes logo-pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.08);
            }
            100% {
                transform: scale(1);
            }
        }
        
        @keyframes tagline-wave {
            0%, 100% {
                transform: translateY(0);
            }
            25% {
                transform: translateY(-2px);
                color: #FF6600;
            }
            75% {
                transform: translateY(2px);
                color: #00b0f0;
            }
        }
        
        /* Responsive aanpassingen */
        @media (max-width: 768px) {
            .logo-floating {
                animation: logo-float 4s ease-in-out infinite;
            }
            
            .logo-pulse {
                animation: logo-pulse 0.8s cubic-bezier(0.455, 0.03, 0.515, 0.955) forwards;
            }
            
            .logo-hover {
                transform: scale(1.03);
            }
            
            .logo-animation-wrapper.active .logo-glow-element {
                opacity: 0.2;
            }
        }
    `;
    document.head.appendChild(style);
})(); 