/* main.js — Header scroll, hero parallax, hero scroll hint, counters, form, mobile nav */

(function () {
  'use strict';

  // ─── Header scroll state ─────────────────────────────────────────────
  const header = document.querySelector('.site-header');
  function onScroll() {
    if (window.scrollY > 60) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Hide scroll hint in hero
    const hint = document.querySelector('.hero-scroll-hint');
    if (hint) {
      if (window.scrollY > 80) hint.classList.add('hidden');
      else hint.classList.remove('hidden');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ─── Hero parallax ──────────────────────────────────────────────────
  const heroInner = document.querySelector('.hero-visual-inner');
  if (heroInner && window.matchMedia('(min-width: 769px)').matches) {
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      const heroH   = document.querySelector('.hero')?.offsetHeight || window.innerHeight;
      if (scrollY < heroH) {
        const pct = scrollY / heroH;
        heroInner.style.transform = `translateY(${pct * 40}px)`;
      }
    }, { passive: true });
  }

  // ─── Stat counter ────────────────────────────────────────────────────
  function animateCounter(el, from, to, duration, suffix) {
    let start = null;
    function step(ts) {
      if (!start) start = ts;
      const progress = Math.min((ts - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
      const current = Math.round(from + (to - from) * eased);
      el.textContent = current + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el     = entry.target;
          const to     = parseInt(el.dataset.count, 10);
          const suffix = el.dataset.suffix || '';
          animateCounter(el, 0, to, 1800, suffix);
          counterObserver.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(c => counterObserver.observe(c));
  }

  // ─── Form interactions ───────────────────────────────────────────────
  const formFields = document.querySelectorAll('.form-field');
  formFields.forEach(field => {
    const input = field.querySelector('input, textarea');
    if (!input) return;

    function checkValue() {
      if (input.value.trim().length > 0) {
        field.classList.add('has-value');
      } else {
        field.classList.remove('has-value');
      }
    }

    input.addEventListener('input', checkValue);
    input.addEventListener('blur', () => {
      checkValue();
      // Basic validity check
      if (input.type === 'email' && input.value) {
        const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value);
        field.classList.toggle('is-valid', valid);
      } else if (input.value.trim().length > 1) {
        field.classList.add('is-valid');
      }
    });
  });

  // Form submit
  const form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('[type="submit"]');
      if (btn) {
        btn.querySelector('span').textContent = 'Enquiry sent.';
        btn.style.pointerEvents = 'none';
        btn.style.opacity = '0.65';
      }
    });
  }

  // ─── Mobile nav ──────────────────────────────────────────────────────
  const navToggle = document.querySelector('.nav-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  if (navToggle && mobileNav) {
    navToggle.addEventListener('click', () => {
      const isOpen = navToggle.classList.toggle('open');
      mobileNav.classList.toggle('is-open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    mobileNav.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('open');
        mobileNav.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
  }

  // ─── Smooth anchor scroll with offset ────────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top    = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  // ─── FAQ Accordion Toggles ───────────────────────────────────────────
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const trigger = item.querySelector('.faq-trigger');
    if (trigger) {
      trigger.addEventListener('click', () => {
        const isOpen = item.classList.contains('is-open');
        faqItems.forEach(i => i.classList.remove('is-open'));
        if (!isOpen) item.classList.add('is-open');
      });
    }
  });

  // ─── System Pill Selector Buttons ────────────────────────────────────
  const systemPillBtns = document.querySelectorAll('.system-pill-btn');
  const serviceTypeSelect = document.getElementById('serviceType');
  systemPillBtns.forEach(pill => {
    pill.addEventListener('click', () => {
      systemPillBtns.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const value = pill.getAttribute('data-value');
      if (serviceTypeSelect && value) {
        serviceTypeSelect.value = value;
      }
    });
  });

})();

