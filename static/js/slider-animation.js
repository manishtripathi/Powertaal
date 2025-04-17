/**
 * PowerTaal Advanced Slider Animation
 * Geavanceerde slider met 3D effecten, parallax en moderne overgangen
 */

class PowerTaalSlider {
    constructor(options = {}) {
        // Default opties
        this.settings = {
            container: '.slideshow-container',
            slides: '.slide',
            duration: 6000,
            transitionSpeed: 1500,
            effect: 'fade-zoom', // 'fade-zoom', '3d-flip', 'slide-parallax', 'cube', 'kenburns'
            autoplay: true,
            indicators: true,
            arrows: true,
            pauseOnHover: true,
            ...options
        };

        // Slider elementen
        this.container = document.querySelector(this.settings.container);
        this.slides = [...document.querySelectorAll(this.settings.slides)];
        this.slideCount = this.slides.length;
        
        // Huidige slide index
        this.currentIndex = 0;
        
        // Timer voor autoplay
        this.timer = null;
        
        // Initialiseren
        if (this.container && this.slideCount > 0) {
            this.init();
        } else {
            console.error('Slider container of slides niet gevonden!');
        }
    }

    init() {
        // Slider container voorbereiden
        this.container.classList.add('advanced-slider');
        this.container.style.position = 'relative';
        this.container.style.overflow = 'hidden';
        
        // Slides voorbereiden
        this.slides.forEach((slide, index) => {
            slide.dataset.index = index;
            slide.style.position = 'absolute';
            slide.style.top = '0';
            slide.style.left = '0';
            slide.style.width = '100%';
            slide.style.height = '100%';
            slide.style.display = index === 0 ? 'block' : 'block';
            slide.style.opacity = index === 0 ? '1' : '0';
            slide.style.zIndex = index === 0 ? '1' : '0';
            slide.style.transition = `opacity ${this.settings.transitionSpeed}ms ease, transform ${this.settings.transitionSpeed}ms ease`;
            
            // Tekstcontainer animatie voorbereiden
            const textContainer = slide.querySelector('.slide-text-container');
            if (textContainer) {
                textContainer.style.opacity = '0';
                textContainer.style.transform = 'translateY(20px)';
                textContainer.style.transition = `opacity 800ms ease ${this.settings.transitionSpeed/2}ms, transform 800ms ease ${this.settings.transitionSpeed/2}ms`;
            }
        });
        
        // Toont de eerste slide
        this.showSlide(0);
        
        // Navigatie pijlen toevoegen
        if (this.settings.arrows) {
            this.addArrows();
        }
        
        // Indicator bullets toevoegen
        if (this.settings.indicators) {
            this.addIndicators();
        }
        
        // Start autoplay
        if (this.settings.autoplay) {
            this.startAutoplay();
            
            // Pauzeren bij hover als de optie aan staat
            if (this.settings.pauseOnHover) {
                this.container.addEventListener('mouseenter', () => this.pauseAutoplay());
                this.container.addEventListener('mouseleave', () => this.startAutoplay());
            }
        }
        
        // Responsive gedrag
        window.addEventListener('resize', () => this.handleResize());
        
        // Touch swipe ondersteuning
        this.addTouchSupport();
    }
    
    showSlide(index) {
        // Zorgt ervoor dat de index binnen bereik blijft
        if (index < 0) index = this.slideCount - 1;
        if (index >= this.slideCount) index = 0;
        
        // Oude slide verbergen
        if (this.currentIndex !== index) {
            const currentSlide = this.slides[this.currentIndex];
            this.applyExitAnimation(currentSlide);
        }
        
        // Nieuwe slide tonen
        const newSlide = this.slides[index];
        this.applyEntranceAnimation(newSlide);
        
        // Update indicatoren
        if (this.settings.indicators) {
            const indicators = this.container.querySelectorAll('.slider-indicator');
            indicators.forEach((ind, i) => {
                ind.classList.toggle('active', i === index);
            });
        }
        
        // Update huidige index
        this.currentIndex = index;
    }
    
    applyEntranceAnimation(slide) {
        // Reset stijlen
        slide.style.display = 'block';
        slide.style.zIndex = '1';
        
        // Verschillende effecten toepassen op basis van de instellingen
        switch (this.settings.effect) {
            case '3d-flip':
                slide.style.transform = 'rotateY(0deg)';
                slide.style.opacity = '1';
                break;
                
            case 'slide-parallax':
                slide.style.transform = 'translateX(0)';
                slide.style.opacity = '1';
                break;
                
            case 'cube':
                slide.style.transform = 'translateZ(0) rotateY(0)';
                slide.style.opacity = '1';
                break;
                
            case 'kenburns':
                slide.style.transform = 'scale(1)';
                slide.style.opacity = '1';
                break;
                
            case 'fade-zoom':
            default:
                slide.style.transform = 'scale(1)';
                slide.style.opacity = '1';
                break;
        }
        
        // Tekstcontainer animeren (fade-in)
        const textContainer = slide.querySelector('.slide-text-container');
        if (textContainer) {
            setTimeout(() => {
                textContainer.style.opacity = '1';
                textContainer.style.transform = 'translateY(0)';
            }, 100);
        }
        
        // Afbeelding animeren
        const image = slide.querySelector('img');
        if (image) {
            if (this.settings.effect === 'kenburns') {
                image.style.transition = `transform ${this.settings.duration}ms ease`;
                image.style.transform = 'scale(1.1)';
            }
        }
    }
    
    applyExitAnimation(slide) {
        // Verschillende exit animaties toepassen
        switch (this.settings.effect) {
            case '3d-flip':
                slide.style.transform = 'rotateY(-90deg)';
                slide.style.opacity = '0';
                break;
                
            case 'slide-parallax':
                slide.style.transform = 'translateX(-100%)';
                slide.style.opacity = '0';
                break;
                
            case 'cube':
                slide.style.transform = 'translateZ(-100px) rotateY(-90deg)';
                slide.style.opacity = '0';
                break;
                
            case 'kenburns':
                slide.style.transform = 'scale(0.95)';
                slide.style.opacity = '0';
                break;
                
            case 'fade-zoom':
            default:
                slide.style.transform = 'scale(0.95)';
                slide.style.opacity = '0';
                break;
        }
        
        // Tekstcontainer animeren (fade-out)
        const textContainer = slide.querySelector('.slide-text-container');
        if (textContainer) {
            textContainer.style.opacity = '0';
            textContainer.style.transform = 'translateY(20px)';
        }
        
        // Na de transitie de display op none zetten en z-index verlagen
        setTimeout(() => {
            slide.style.zIndex = '0';
        }, this.settings.transitionSpeed);
    }
    
    nextSlide() {
        this.showSlide(this.currentIndex + 1);
    }
    
    prevSlide() {
        this.showSlide(this.currentIndex - 1);
    }
    
    startAutoplay() {
        // Voorkomt meerdere timers
        this.pauseAutoplay();
        
        // Start een nieuwe timer
        this.timer = setInterval(() => {
            this.nextSlide();
        }, this.settings.duration);
    }
    
    pauseAutoplay() {
        if (this.timer) {
            clearInterval(this.timer);
            this.timer = null;
        }
    }
    
    addArrows() {
        // Pijlen container
        const arrowsContainer = document.createElement('div');
        arrowsContainer.className = 'slider-arrows';
        
        // Previous pijl
        const prevArrow = document.createElement('button');
        prevArrow.className = 'slider-arrow slider-arrow-prev';
        prevArrow.innerHTML = '<i class="fas fa-chevron-left"></i>';
        prevArrow.setAttribute('aria-label', 'Vorige slide');
        prevArrow.addEventListener('click', () => this.prevSlide());
        
        // Next pijl
        const nextArrow = document.createElement('button');
        nextArrow.className = 'slider-arrow slider-arrow-next';
        nextArrow.innerHTML = '<i class="fas fa-chevron-right"></i>';
        nextArrow.setAttribute('aria-label', 'Volgende slide');
        nextArrow.addEventListener('click', () => this.nextSlide());
        
        // Toevoegen aan container
        arrowsContainer.appendChild(prevArrow);
        arrowsContainer.appendChild(nextArrow);
        this.container.appendChild(arrowsContainer);
        
        // Stijlen toevoegen
        const style = document.createElement('style');
        style.textContent = `
            .slider-arrows {
                position: absolute;
                width: 100%;
                top: 50%;
                transform: translateY(-50%);
                z-index: 10;
                display: flex;
                justify-content: space-between;
                pointer-events: none;
            }
            .slider-arrow {
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background-color: rgba(0, 0, 0, 0.5);
                color: white;
                border: none;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 10px;
                transition: all 0.3s ease;
                opacity: 0.7;
                pointer-events: auto;
            }
            .slider-arrow:hover {
                background-color: rgba(0, 176, 240, 0.8);
                opacity: 1;
                transform: scale(1.1);
            }
            .slider-arrow:focus {
                outline: none;
                box-shadow: 0 0 0 3px rgba(0, 176, 240, 0.5);
            }
            .slider-arrow i {
                font-size: 16px;
            }
        `;
        document.head.appendChild(style);
    }
    
    addIndicators() {
        // Indicators container
        const indicatorsContainer = document.createElement('div');
        indicatorsContainer.className = 'slider-indicators';
        
        // Indicators toevoegen
        for (let i = 0; i < this.slideCount; i++) {
            const indicator = document.createElement('button');
            indicator.className = 'slider-indicator';
            if (i === 0) indicator.classList.add('active');
            indicator.setAttribute('aria-label', `Slide ${i + 1}`);
            indicator.addEventListener('click', () => this.showSlide(i));
            indicatorsContainer.appendChild(indicator);
        }
        
        // Toevoegen aan container
        this.container.appendChild(indicatorsContainer);
        
        // Stijlen toevoegen
        const style = document.createElement('style');
        style.textContent = `
            .slider-indicators {
                position: absolute;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 10;
                display: flex;
                gap: 10px;
            }
            .slider-indicator {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background-color: rgba(255, 255, 255, 0.5);
                border: none;
                cursor: pointer;
                transition: all 0.3s ease;
                padding: 0;
                margin: 0;
            }
            .slider-indicator.active {
                background-color: white;
                transform: scale(1.2);
            }
            .slider-indicator:hover {
                background-color: rgba(255, 255, 255, 0.8);
            }
            .slider-indicator:focus {
                outline: none;
                box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.5);
            }
        `;
        document.head.appendChild(style);
    }
    
    handleResize() {
        // Hier kun je responsieve aanpassingen doen
        const windowWidth = window.innerWidth;
        
        // Aanpassen van de pijlen op kleinere schermen
        const arrows = this.container.querySelectorAll('.slider-arrow');
        arrows.forEach(arrow => {
            if (windowWidth < 768) {
                arrow.style.width = '30px';
                arrow.style.height = '30px';
            } else {
                arrow.style.width = '40px';
                arrow.style.height = '40px';
            }
        });
    }
    
    addTouchSupport() {
        let touchstartX = 0;
        let touchendX = 0;
        
        this.container.addEventListener('touchstart', e => {
            touchstartX = e.changedTouches[0].screenX;
        }, { passive: true });
        
        this.container.addEventListener('touchend', e => {
            touchendX = e.changedTouches[0].screenX;
            this.handleSwipe();
        }, { passive: true });
        
        this.handleSwipe = () => {
            const threshold = 50; // Minimale veeg afstand
            if (touchendX < touchstartX - threshold) {
                this.nextSlide(); // Naar links vegen
            }
            if (touchendX > touchstartX + threshold) {
                this.prevSlide(); // Naar rechts vegen
            }
        };
    }
}

// Extra CSS voor geavanceerde effecten toevoegen
(function addAdvancedStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .advanced-slider {
            perspective: 1000px;
            transform-style: preserve-3d;
        }
        
        .advanced-slider .slide {
            backface-visibility: hidden;
        }
        
        /* 3D Flip effect */
        .advanced-slider[data-effect="3d-flip"] .slide {
            transform-origin: center center;
            transform: rotateY(90deg);
            transition: transform 1.5s ease, opacity 1.5s ease;
        }
        
        /* Slide parallax effect */
        .advanced-slider[data-effect="slide-parallax"] .slide {
            transform: translateX(100%);
            transition: transform 1.5s ease, opacity 1.5s ease;
        }
        
        .advanced-slider[data-effect="slide-parallax"] .slide-text-container {
            transform: translateX(50px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }
        
        /* Cube effect */
        .advanced-slider[data-effect="cube"] {
            perspective: 1200px;
        }
        
        .advanced-slider[data-effect="cube"] .slide {
            transform-origin: 100% 50%;
            transform: translateZ(100px) rotateY(90deg);
            transition: transform 1.5s ease, opacity 1.5s ease;
        }
        
        /* Ken Burns effect */
        .advanced-slider[data-effect="kenburns"] .slide img {
            transform-origin: center center;
            transition: transform 6s ease;
        }
        
        /* Fade Zoom effect */
        .advanced-slider[data-effect="fade-zoom"] .slide {
            transform: scale(1.05);
            transition: transform 1.5s ease, opacity 1.5s ease;
        }
        
        .advanced-slider .slide-text-container h1 {
            transition: transform 0.6s ease 0.3s, opacity 0.6s ease 0.3s;
        }
    `;
    document.head.appendChild(style);
})();

// Initialiseer de slider wanneer de pagina geladen is
document.addEventListener('DOMContentLoaded', () => {
    // Controleer of er sliders op de pagina zijn
    const slideContainer = document.querySelector('.slideshow-container');
    const slides = document.querySelectorAll('.slide');

    if (slideContainer && slides.length > 0) {
        console.log('PowerTaal Slider: Initializing slider with ' + slides.length + ' slides');
        
        // Zorg ervoor dat alle slides zichtbaar zijn
        slides.forEach((slide, index) => {
            slide.style.display = 'block';
            // Alleen de eerste slide moet zichtbaar zijn (opacity 1)
            slide.style.opacity = index === 0 ? '1' : '0';
        });
        
        // Alle sliders op de pagina initialiseren
        const slider = new PowerTaalSlider({
            container: '.slideshow-container',
            slides: '.slide',
            duration: 6000,         // Tijd tussen slides in ms
            transitionSpeed: 1200,  // Overgangssnelheid in ms
            effect: '3d-flip',      // Effect: 'fade-zoom', '3d-flip', 'slide-parallax', 'cube', 'kenburns'
            autoplay: true,
            indicators: true,
            arrows: true,
            pauseOnHover: true
        });
        
        // Effect wisselen elke 2 slides (voor demo-doeleinden)
        const effects = ['fade-zoom', '3d-flip', 'slide-parallax', 'cube', 'kenburns'];
        let effectIndex = 0;
        
        // Voeg een speciaal effect toe dat de effecten afwisselt voor een demo
        function changeEffect() {
            effectIndex = (effectIndex + 1) % effects.length;
            slider.settings.effect = effects[effectIndex];
            slider.container.setAttribute('data-effect', effects[effectIndex]);
            
            // Toon een korte notificatie over het actieve effect
            const notification = document.createElement('div');
            notification.className = 'effect-notification';
            notification.textContent = `Effect: ${effects[effectIndex]}`;
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.opacity = '0';
                setTimeout(() => {
                    document.body.removeChild(notification);
                }, 500);
            }, 2000);
        }
        
        // Wissel effect elke 3 slides
        let slideCounter = 0;
        const originalNextSlide = slider.nextSlide.bind(slider);
        slider.nextSlide = function() {
            originalNextSlide();
            slideCounter++;
            if (slideCounter % 3 === 0) {
                changeEffect();
            }
        };
    } else {
        console.warn('PowerTaal Slider: No slideshow container or slides found on this page.');
    }
    
    // Voeg stijl toe voor de notificatie
    const notificationStyle = document.createElement('style');
    notificationStyle.textContent = `
        .effect-notification {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: rgba(0, 176, 240, 0.9);
            color: white;
            padding: 10px 15px;
            border-radius: 4px;
            font-size: 14px;
            z-index: 9999;
            transition: opacity 0.5s ease;
        }
    `;
    document.head.appendChild(notificationStyle);
}); 