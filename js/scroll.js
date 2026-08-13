/* scroll.js — IntersectionObserver reveals + sticky services section */

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
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => revealObserver.observe(el));
  }

  // ─── Sticky Services Section ────────────────────────────────────────
  const serviceItems   = document.querySelectorAll('.service-item');
  const serviceVisuals = document.querySelectorAll('.service-visual');
  const currentName    = document.querySelector('.services-current-name');
  const progressItems  = document.querySelectorAll('.services-progress-item');

  function activateService(index) {
    serviceVisuals.forEach((v, i) => {
      v.classList.toggle('is-active', i === index);
    });

    progressItems.forEach((p, i) => {
      p.classList.toggle('is-active', i === index);
      p.classList.toggle('is-past', i < index);
    });

    if (currentName && serviceItems[index]) {
      const title = serviceItems[index].querySelector('.service-title');
      if (title) {
        currentName.style.opacity = '0';
        setTimeout(() => {
          currentName.textContent = title.textContent;
          currentName.style.opacity = '1';
        }, 200);
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
    }, { threshold: 0.4, rootMargin: '0px 0px -20% 0px' });

    serviceItems.forEach(item => serviceObserver.observe(item));

    // Initialize first
    activateService(0);
  }

})();
