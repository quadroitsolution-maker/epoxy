/* scroll.js — IntersectionObserver reveals + sticky services section with dynamic color shifts */

(function () {
  'use strict';

  // ─── Scroll Reveal ─────────────────────────────────────────────────
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

    revealEls.forEach(el => revealObserver.observe(el));
  }

  // ─── Sticky Services Section Dynamic Color Shift ───────────────────
  const servicesSection = document.querySelector('.section-services');
  const serviceItems     = document.querySelectorAll('.service-item');
  const serviceVisuals   = document.querySelectorAll('.service-visual');
  const currentName      = document.querySelector('.services-current-name');
  const progressItems    = document.querySelectorAll('.services-progress-item');

  const serviceBgColors = [
    'linear-gradient(180deg, #0B132B 0%, #0F0C1B 50%, #08070D 100%)', // 0: Metallic Epoxy
    'linear-gradient(180deg, #08070D 0%, #0A1124 50%, #0D162C 100%)', // 1: Flake Systems
    'linear-gradient(180deg, #0D162C 0%, #121B2A 50%, #0F1722 100%)', // 2: Polished Concrete
    'linear-gradient(180deg, #0F1722 0%, #12141A 50%, #0B132B 100%)'  // 3: Industrial Coatings
  ];

  function activateService(index) {
    serviceVisuals.forEach((v, i) => {
      v.classList.toggle('is-active', i === index);
    });

    progressItems.forEach((p, i) => {
      p.classList.toggle('is-active', i === index);
      p.classList.toggle('is-past', i < index);
    });

    if (servicesSection && serviceBgColors[index]) {
      servicesSection.style.background = serviceBgColors[index];
    }

    if (currentName && serviceItems[index]) {
      const title = serviceItems[index].querySelector('.service-title');
      if (title) {
        currentName.style.opacity = '0';
        setTimeout(() => {
          currentName.textContent = title.textContent;
          currentName.style.opacity = '1';
        }, 180);
      }
    }
  }

  if (serviceItems.length && serviceVisuals.length) {
    const serviceObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const index = Array.from(serviceItems).indexOf(entry.target);
          if (index !== -1) activateService(index);
        }
      });
    }, { threshold: 0.35, rootMargin: '0px 0px -15% 0px' });

    serviceItems.forEach(item => serviceObserver.observe(item));

    // Initialize first
    activateService(0);
  }

  // ─── Active Nav Link Observer ────────────────────────────────────────
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  if (sections.length && navLinks.length) {
    const navObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === '#' + id) {
              link.style.color = 'var(--color-accent)';
            } else {
              link.style.color = '';
            }
          });
        }
      });
    }, { threshold: 0.25 });

    sections.forEach(s => navObserver.observe(s));
  }

})();
