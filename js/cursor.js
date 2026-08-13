/* cursor.js — Custom cursor behavior with Funky Metallic Particle Sparkle Trail */

(function () {
  'use strict';

  // Respect reduced motion & touch screens
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches ||
      window.matchMedia('(hover: none), (pointer: coarse)').matches) {
    return;
  }

  const cursor = document.querySelector('.cursor');
  const ring   = document.querySelector('.cursor-ring');
  if (!cursor || !ring) return;

  let mx = 0, my = 0;
  let rx = 0, ry = 0;
  let lastX = 0, lastY = 0;

  const funkyColors = ['#F5D77F', '#60A8F8', '#C084FC', '#34D399', '#FF6B6B', '#F472B6'];

  // Spawn funky sparkle trail
  function createSparkle(x, y) {
    const sparkle = document.createElement('div');
    sparkle.className = 'funky-sparkle';

    const color = funkyColors[Math.floor(Math.random() * funkyColors.length)];
    const size = Math.random() * 6 + 4; // 4px to 10px
    const vx = (Math.random() - 0.5) * 40; // float offset X
    const vy = (Math.random() - 0.7) * 50; // float up offset Y

    sparkle.style.left = x + 'px';
    sparkle.style.top = y + 'px';
    sparkle.style.width = size + 'px';
    sparkle.style.height = size + 'px';
    sparkle.style.backgroundColor = color;
    sparkle.style.boxShadow = `0 0 ${size * 2}px ${color}`;
    sparkle.style.setProperty('--vx', vx + 'px');
    sparkle.style.setProperty('--vy', vy + 'px');

    document.body.appendChild(sparkle);

    setTimeout(() => {
      sparkle.remove();
    }, 800);
  }

  // Track mouse and emit sparkles
  document.addEventListener('mousemove', (e) => {
    mx = e.clientX;
    my = e.clientY;
    cursor.style.left = mx + 'px';
    cursor.style.top  = my + 'px';

    const dist = Math.hypot(mx - lastX, my - lastY);
    if (dist > 18) {
      createSparkle(mx, my);
      lastX = mx;
      lastY = my;
    }
  });

  // Smooth ring follow
  function animateRing() {
    rx += (mx - rx) * 0.14;
    ry += (my - ry) * 0.14;
    ring.style.left = rx + 'px';
    ring.style.top  = ry + 'px';
    requestAnimationFrame(animateRing);
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
