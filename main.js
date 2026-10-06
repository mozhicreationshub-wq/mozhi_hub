document.addEventListener('DOMContentLoaded', () => {
  // 1. Scroll-Triggered Micro-Animations
  const revealElements = document.querySelectorAll('.scroll-reveal');
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, {
    root: null,
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // 2. Smooth Page Transitions
  // Add base fade class to wrapper
  const wrapper = document.getElementById('main-content-wrapper');
  if (wrapper) {
    wrapper.classList.add('page-fade');
  }

  const links = document.querySelectorAll('a[href]');
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      
      // Only intercept internal html links
      if (href && href.endsWith('.html') && !link.hasAttribute('target')) {
        e.preventDefault();
        
        if (wrapper) {
          wrapper.classList.add('fade-out');
        } else {
          document.body.classList.add('fade-out'); // fallback
        }
        
        setTimeout(() => {
          window.location.href = href;
        }, 400); // Matches CSS transition duration
      }
    });
  });

  // 3. Form Validation and Success State
  const form = document.getElementById('inquiry-form');
  const successState = document.getElementById('success-state');
  
  if (form && successState) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Basic validation is handled by HTML5 'required' attributes.
      // We can add custom validation here if needed.
      
      // Transition out form
      form.style.opacity = '0';
      form.style.transition = 'opacity 0.5s ease';
      
      setTimeout(() => {
        form.classList.add('hidden');
        
        // Show success state
        successState.classList.remove('hidden');
        // Small delay to ensure display:flex is applied before opacity transition
        setTimeout(() => {
          successState.classList.remove('opacity-0');
        }, 50);
      }, 500);
    });
  }

  // 4. Interactive Service Modal
  const serviceCards = document.querySelectorAll('.service-card');
  const modal = document.getElementById('service-modal');
  if (serviceCards.length > 0 && modal) {
    const backdrop = document.getElementById('service-modal-backdrop');
    const content = document.getElementById('service-modal-content');
    const closeBtn = document.getElementById('service-modal-close');
    const modalBody = document.getElementById('service-modal-body');

    const serviceData = {
      'general': {
        title: 'Comprehensive Digital Solution',
        text: 'From initial architecture planning to pixel-perfect design and backend engineering, we manage the entire lifecycle of your digital product. We focus on scalability, maintainability, and top-tier performance.'
      },
      'grow': {
        title: 'Search & Social Reach',
        text: 'Get your business in front of people actively searching for what you offer, with calculated and elegant Google and Meta advertising campaigns.'
      }
    };

    const openModal = (serviceId) => {
      const data = serviceData[serviceId] || serviceData['general'];
      modalBody.innerHTML = `
        <h3 class="font-display text-3xl mb-4 text-heritage-charcoal">${data.title}</h3>
        <p class="font-body text-lg text-heritage-muted">${data.text}</p>
        <button class="mt-8 font-sans text-xs uppercase tracking-widest font-semibold text-heritage-ivory bg-heritage-charcoal hover:bg-heritage-green px-8 py-3 transition-colors" onclick="window.location.href='contact.html'">Inquire Now</button>
      `;
      
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      
      // Small delay to allow display:flex to apply before transition
      setTimeout(() => {
        backdrop.classList.remove('opacity-0');
        content.classList.remove('opacity-0', 'translate-y-8');
      }, 50);
    };

    const closeModal = () => {
      backdrop.classList.add('opacity-0');
      content.classList.add('opacity-0', 'translate-y-8');
      
      setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }, 300); // Wait for transition
    };

    serviceCards.forEach(card => {
      card.addEventListener('click', () => {
        const serviceId = card.getAttribute('data-service') || 'general';
        openModal(serviceId);
      });
    });

    closeBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', closeModal);
  }
});
