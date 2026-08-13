/* cursor.js — Custom cursor behavior */

(function () {
  'use strict';

  const cursor = document.querySelector('.cursor');
  const ring   = document.querySelector('.cursor-ring');
  if (!cursor || !ring) return;

  let mx = 0, my = 0;
  let rx = 0, ry = 0;
  let rafId = null;

  // Track mouse
  document.addEventListener('mousemove', (e) => {
    mx = e.clientX;
    my = e.clientY;
    cursor.style.left = mx + 'px';
    cursor.style.top  = my + 'px';
  });

  // Smooth ring follow
  function animateRing() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    ring.style.left = rx + 'px';
    ring.style.top  = ry + 'px';
    rafId = requestAnimationFrame(animateRing);
  }
  animateRing();

  // Cursor states for interactive elements
  const hoverEls = document.querySelectorAll('a, button, .nav-link, .btn-primary, .btn-outline, .why-pillar, .process-step');
  hoverEls.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.classList.add('is-hovering');
      ring.classList.add('is-hovering');
    });
    el.addEventListener('mouseleave', () => {
      cursor.classList.remove('is-hovering');
      ring.classList.remove('is-hovering');
    });
  });

  // Gallery cursor state
  const galleryItems = document.querySelectorAll('.gallery-item');
  galleryItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
      cursor.classList.add('is-gallery');
      ring.classList.add('is-gallery');
      cursor.classList.remove('is-hovering');
      ring.classList.remove('is-hovering');
    });
    item.addEventListener('mouseleave', () => {
      cursor.classList.remove('is-gallery');
      ring.classList.remove('is-gallery');
    });
  });

  // Hide cursor when leaving window
  document.addEventListener('mouseleave', () => {
    cursor.style.opacity = '0';
    ring.style.opacity = '0';
  });
  document.addEventListener('mouseenter', () => {
    cursor.style.opacity = '';
    ring.style.opacity = '';
  });
})();
