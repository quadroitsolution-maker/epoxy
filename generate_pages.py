import re

# Template for Head
head_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  
  <!-- Google Fonts: DM Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
  
  <!-- CSS -->
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
"""

# Template for Header and Navigation
header_template = """
  <!-- ═══════════════════════════════════════
       HEADER & NAVIGATION
  ═══════════════════════════════════════ -->
  <header class="site-header" id="header">
    <div class="container header-inner">
      <!-- Logo -->
      <a href="index.html" class="logo-brand" aria-label="Rapid Epoxy Home">
        <div class="logo-monogram">RE</div>
        <span>Rapid Epoxy</span>
      </a>

      <!-- Desktop Nav -->
      <nav aria-label="Primary Navigation">
        <ul class="nav-menu">
          <li><a href="index.html" class="nav-link">Home</a></li>
          <li><a href="products.html" class="nav-link">Products &amp; Finishes ▾</a></li>
          <li><a href="services.html" class="nav-link">Services ▾</a></li>
          <li><a href="about.html" class="nav-link">About &amp; Contact ▾</a></li>
        </ul>
      </nav>

      <!-- Header Actions -->
      <div style="display:flex; align-items:center; gap:var(--space-3);">
        <a href="about.html#contact" class="btn btn-gold">Request Quote</a>
        <!-- Avatar icon -->
        <a href="account.html" style="width:36px;height:36px;border-radius:50%;background:var(--color-teal-light);display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;" aria-label="Account">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-teal)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
          </svg>
        </a>
      </div>

      <!-- Mobile Toggle -->
      <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle mobile menu">☰</button>
    </div>
  </header>

  <!-- Mobile Menu Drawer Overlay -->
  <div class="mobile-menu-overlay" id="mobileMenu">
    <a href="index.html" class="mobile-nav-link">Home</a>
    <a href="products.html" class="mobile-nav-link">Products &amp; Finishes</a>
    <a href="services.html" class="mobile-nav-link">Our Services</a>
    <a href="about.html" class="mobile-nav-link">About Us &amp; Contact</a>
    <a href="about.html#contact" class="btn btn-gold" style="margin-top:var(--space-4);">Request Quote</a>
  </div>
  
  <main id="main-content">
"""

# Template for Footer
footer_template = """
  </main>
  
  <!-- ═══════════════════════════════════════
       FOOTER
  ═══════════════════════════════════════ -->
  <footer class="site-footer">
    <div class="container">
      
      <div class="footer-grid">
        
        <!-- Brand Info -->
        <div>
          <a href="index.html" class="logo-brand">
            <div class="logo-monogram">RE</div>
            <span>Rapid Epoxy</span>
          </a>
          <p class="footer-brand-desc">
            Victorian licensed epoxy flooring contractors delivering industrial-grade resin finishes for residential and commercial spaces.
          </p>
        </div>

        <!-- Solutions Column -->
        <div>
          <h4 class="footer-col-title">Systems</h4>
          <ul class="footer-links">
            <li><a href="products.html">Vinyl Flakes</a></li>
            <li><a href="products.html">Hybrid Stone</a></li>
            <li><a href="products.html">3D Metallic Resin</a></li>
            <li><a href="products.html">Industrial Solid</a></li>
          </ul>
        </div>

        <!-- Company Column -->
        <div>
          <h4 class="footer-col-title">Company</h4>
          <ul class="footer-links">
            <li><a href="about.html">About Our Team</a></li>
            <li><a href="products.html#packages">Fixed Pricing</a></li>
            <li><a href="services.html#prep">Diamond Prep Process</a></li>
          </ul>
        </div>

        <!-- Support Column -->
        <div>
          <h4 class="footer-col-title">Assurance</h4>
          <ul class="footer-links">
            <li><a href="about.html#contact">10-Year Warranty</a></li>
            <li><a href="about.html#contact">Moisture Barrier Test</a></li>
            <li><a href="about.html#contact">VIC License Details</a></li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom">
        <span>© 2026 Rapid Epoxy Solutions Pty Ltd. All rights reserved. VIC Lic #48291.</span>
        <div style="display:flex; gap:var(--space-4);">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>

    </div>
  </footer>

  <!-- ═══════════════════════════════════════
       FLOATING WHATSAPP BUTTON
  ═══════════════════════════════════════ -->
  <a href="https://wa.me/61390004821?text=Hi%20Rapid%20Epoxy%2C%20I'm%20interested%20in%20a%20quote%20for%20my%20floor." 
     target="_blank" 
     rel="noopener" 
     class="floating-whatsapp-btn" 
     aria-label="Chat on WhatsApp">
    💬
  </a>

  <!-- JS Script -->
  <script>
    // Header shadow on scroll
    const header = document.getElementById('header');
    if (header) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
      });
    }

    // Mobile Menu Toggle Drawer
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileMenu   = document.getElementById('mobileMenu');
    if (mobileToggle && mobileMenu) {
      mobileToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('is-active');
        mobileToggle.textContent = mobileMenu.classList.contains('is-active') ? '✕' : '☰';
      });

      // Close menu on link click
      document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', () => {
          mobileMenu.classList.remove('is-active');
          mobileToggle.textContent = '☰';
        });
      });
    }

    // Scroll Reveal Observer
    const revealEls = document.querySelectorAll('.reveal');
    if (revealEls.length) {
      const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

      revealEls.forEach(el => revealObserver.observe(el));
    }

    // Category Tabs Switching (Vinyl Flakes vs Hybrid Stone)
    const tabFlakes = document.getElementById('tab-flakes');
    const tabStone  = document.getElementById('tab-stone');
    if (tabFlakes && tabStone) {
      tabFlakes.addEventListener('click', () => {
        tabFlakes.classList.add('active');
        tabStone.classList.remove('active');
      });
      tabStone.addEventListener('click', () => {
        tabStone.classList.add('active');
        tabFlakes.classList.remove('active');
      });
    }

    // Option items selection logic for Garage Packages
    document.querySelectorAll('.garage-options-list').forEach(list => {
      const priceDisplay = list.parentElement.querySelector('.package-price');
      const items = list.querySelectorAll('.option-item');
      
      items.forEach(item => {
        item.addEventListener('click', () => {
          items.forEach(i => i.classList.remove('selected'));
          item.classList.add('selected');
          if (priceDisplay && item.dataset.price) {
            priceDisplay.textContent = item.dataset.price;
          }
        });
      });
    });

    // Form Submit Handler
    function handleFormSubmit(e) {
      e.preventDefault();
      alert('Thank you for reaching out to Rapid Epoxy! We have received your inquiry and will contact you within 2 hours.');
    }

    // Send Form Details via WhatsApp Redirect
    function sendViaWhatsApp() {
      const name = document.getElementById('fullName') ? document.getElementById('fullName').value : '';
      const phone = document.getElementById('phoneNumber') ? document.getElementById('phoneNumber').value : '';
      const service = document.getElementById('serviceType') ? document.getElementById('serviceType').value : '';
      const details = document.getElementById('projectDetails') ? document.getElementById('projectDetails').value : '';

      const msg = `Hi Rapid Epoxy! My name is ${name || 'Customer'} (${phone || 'N/A'}). I am interested in ${service || 'a quote'}. Details: ${details || 'General inquiry'}`;
      const encodedMsg = encodeURIComponent(msg);
      window.open(`https://wa.me/61390004821?text=${encodedMsg}`, '_blank');
    }
  </script>
</body>
</html>
"""

# index.html
index_content = head_template.format(
    title="Rapid Epoxy — Home", 
    description="Melbourne's trusted epoxy flooring specialists. High-grade garage flake systems, metallic resin pours, and diamond-ground concrete resurfacing with a 10-year warranty."
) + header_template + """
    <!-- ═══════════════════════════════════════
         HERO SECTION
    ═══════════════════════════════════════ -->
    <section class="hero-section" id="hero">
      <div class="container">
        
        <!-- Hero Media Wrap -->
        <div class="hero-media-wrap">
          <img src="img/hero_epoxy.jpg" alt="Architectural Metallic Epoxy Floor Pour" class="hero-img">
          
          <div class="hero-overlay-content">
            <span class="eyebrow">— Greater Melbourne &amp; Victoria</span>
            <h1 class="hero-headline">Industrial-Grade Epoxy Floors. Built for Life.</h1>
            <p class="hero-sub">
              Diamond-ground substrate prep, 100% solid resin, and UV-stable polyaspartic topcoats. Engineered for seamless garage, commercial, and retail surfaces.
            </p>
            <div>
              <a href="about.html#contact" class="btn btn-gold">
                Get a Fixed Quote <span style="font-size:1.1rem; line-height:1;">→</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 3 Feature Accessibility Cards -->
        <div class="hero-cards-grid">
          
          <!-- Card 1 -->
          <div class="hero-card reveal" data-delay="1">
            <div>
              <div class="hero-card-icon">
                <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
              </div>
              <h2 class="hero-card-title">Finishes &amp; Color Palette</h2>
              <p class="hero-card-desc">
                Granite vinyl flakes, solid industrial coatings, and custom 3D metallic quartz resin finishes.
              </p>
            </div>
            <a href="products.html#colours" class="hero-card-link">View Finishes →</a>
          </div>

          <!-- Card 2 (Featured Teal) -->
          <div class="hero-card card-featured reveal" data-delay="2">
            <div>
              <div class="hero-card-icon">
                <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
              </div>
              <h2 class="hero-card-title">Instant Fixed Estimate</h2>
              <p class="hero-card-desc">
                Receive an itemized quote for your 1, 2, or 3-car garage within 2 hours. Zero hidden site fees.
              </p>
            </div>
            <a href="about.html#contact" class="hero-card-link">Contact Us →</a>
          </div>

          <!-- Card 3 -->
          <div class="hero-card reveal" data-delay="3">
            <div>
              <div class="hero-card-icon">
                <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <h2 class="hero-card-title">Garage Packages</h2>
              <p class="hero-card-desc">
                Complete systems with 100% flake broadcast and 10-year structural warranty starting from $1,650.
              </p>
            </div>
            <a href="products.html#packages" class="hero-card-link">See Pricing →</a>
          </div>

        </div>

        <!-- Authentic Trust Proof Bar -->
        <div class="trust-bar reveal" data-delay="2">
          <div class="trust-item">
            <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>4.9 / 5 Rating (140+ Reviews)</span>
          </div>
          <div class="trust-item">
            <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>10-Year Structural Warranty</span>
          </div>
          <div class="trust-item">
            <svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            <span>48-Hour Rapid Cure</span>
          </div>
          <div class="trust-item">
            <svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            <span>VIC License #48291</span>
          </div>
        </div>

      </div>
    </section>
""" + footer_template

# products.html
products_content = head_template.format(
    title="Rapid Epoxy — Products & Packages", 
    description="Discover our range of premium epoxy flooring products including metallic systems, solid monolithic, vinyl flakes, and specialized garage packages."
) + header_template + """
    <!-- ═══════════════════════════════════════
         PRODUCTS HEADER
    ═══════════════════════════════════════ -->
    <section class="section-packages" style="padding-top: var(--space-24); background: var(--color-teal); color: white;">
      <div class="container">
         <div class="packages-header" style="text-align:center; max-width: 800px; margin:0 auto; padding-bottom:var(--space-12);">
           <span class="eyebrow" style="color:var(--color-gold);">SYSTEM ARCHITECTURE</span>
           <h1 class="section-title" style="color: white; margin-top: var(--space-2);">High-Performance Flooring Matrix</h1>
           <p class="section-desc" style="color: rgba(255,255,255,0.8);">
             Engineered surfaces designed for specific environmental demands. Select the optimal coating system based on chemical resistance, load-bearing requirements, and aesthetic intent.
           </p>
         </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════
         TYPES OF EPOXY FLOORING
    ═══════════════════════════════════════ -->
    <section class="section-services">
      <div class="container">
        <div class="services-grid">
          <!-- Metallic System -->
          <div class="service-card">
            <span class="service-badge">Architectural Grade</span>
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            </div>
            <h3 class="service-card-title">Metallic System Resin</h3>
            <p class="service-card-desc">
              A highly decorative, self-leveling system that creates three-dimensional depth and unique organic flow patterns.
            </p>
            <div class="service-thumb-wrap">
              <img src="img/metallic_epoxy.jpg" alt="Metallic System Resin" class="service-thumb">
            </div>
          </div>
          <!-- Solid Monolithic -->
          <div class="service-card">
            <span class="service-badge">Industrial Grade</span>
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
            </div>
            <h3 class="service-card-title">Solid Monolithic Coating</h3>
            <p class="service-card-desc">
              High-build, 100% solid epoxy coating providing exceptional durability, chemical resistance, and a seamless surface.
            </p>
            <div class="service-thumb-wrap">
              <img src="img/plain_epoxy.jpg" alt="Solid Monolithic" class="service-thumb">
            </div>
          </div>
          <!-- Vinyl Flake -->
          <div class="service-card">
            <span class="service-badge">Commercial Grade</span>
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <h3 class="service-card-title">Vinyl Flake Broadcast</h3>
            <p class="service-card-desc">
              A multi-layer system incorporating colored vinyl chips sealed with a polyaspartic topcoat. Exceptional abrasion resistance.
            </p>
            <div class="service-thumb-wrap">
              <img src="img/flake_epoxy.jpg" alt="Vinyl Flake" class="service-thumb">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════
         COLOUR PALETTE & DESIGNS
    ═══════════════════════════════════════ -->
    <section class="section-services" style="background: var(--color-surface-sub);" id="colours">
      <div class="container">
        <div class="services-top-bar">
          <div>
            <span class="eyebrow">AESTHETIC ENGINEERING</span>
            <h2 class="section-title">Color Palette &amp; Designs</h2>
            <p class="section-desc">
              The foundation of your space sets the tone. Our curated selection of solid colors, metallic finishes, and multi-dimensional flake blends.
            </p>
          </div>
        </div>

        <!-- Solid Colors Preview -->
        <h3 style="margin-bottom: var(--space-4);">Solid Color Standards</h3>
        <p style="margin-bottom: var(--space-6); color: var(--color-muted); max-width: 600px;">
          Formulated for maximum opacity and UV stability. Custom color matching to RAL or Pantone available.
        </p>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-6); margin-bottom: var(--space-12);">
          <div>
            <div style="height:150px; background:#D9DADA; border-radius:var(--radius-sm); margin-bottom:var(--space-2);"></div>
            <strong>PLATINUM GRAY</strong><br><small style="color:var(--color-muted);">SKU: SS-012</small>
          </div>
          <div>
            <div style="height:150px; background:#8590A2; border-radius:var(--radius-sm); margin-bottom:var(--space-2);"></div>
            <strong>INDUSTRIAL BLUE</strong><br><small style="color:var(--color-muted);">SKU: SS-045</small>
          </div>
          <div>
            <div style="height:150px; background:#CDA97D; border-radius:var(--radius-sm); margin-bottom:var(--space-2);"></div>
            <strong>DESERT TAN</strong><br><small style="color:var(--color-muted);">SKU: SS-088</small>
          </div>
          <div>
            <div style="height:150px; background:#294943; border-radius:var(--radius-sm); margin-bottom:var(--space-2);"></div>
            <strong>SAFETY GREEN</strong><br><small style="color:var(--color-muted);">SKU: SS-102</small>
          </div>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-8); align-items:center;">
          <div>
            <img src="img/hero_epoxy.jpg" alt="Custom Design & Integration" style="width:100%; border-radius:var(--radius-md);">
          </div>
          <div>
            <span class="eyebrow">BESPOKE SOLUTIONS</span>
            <h2 class="section-title">Custom Design &amp; Integration</h2>
            <p class="section-desc">
              Your facility is unique, and your flooring can be too. We specialize in custom design integrations that go beyond standard colors.
            </p>
            <ul class="service-checklist" style="margin-top:var(--space-6);">
              <li>Corporate Logo Integration</li>
              <li>Safety &amp; Traffic Demarcation Lines</li>
              <li>Custom Color Matching (RAL/Pantone)</li>
              <li>Multi-System Zoning</li>
            </ul>
            <a href="about.html#contact" class="btn btn-outline-teal" style="margin-top: var(--space-6);">Consult on a Custom Design →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════
         POPULAR GARAGE PACKAGES
    ═══════════════════════════════════════ -->
    <section class="section-packages" id="packages">
      <div class="container">
        
        <div class="packages-header">
          <div>
            <h2 class="section-title">Popular Garage Packages</h2>
            <p class="section-desc">
              Transparent, comprehensive pricing for our most requested high-performance floor systems. All packages include diamond grinding, base coat, flake broadcast, and UV-stable polyaspartic topcoat.
            </p>
          </div>

          <!-- Package Category Selector Tabs -->
          <div class="packages-tabs" role="tablist">
            <button class="tab-btn active" id="tab-flakes" role="tab" aria-selected="true">Vinyl Flakes</button>
            <button class="tab-btn" id="tab-stone" role="tab" aria-selected="false">Hybrid Stone</button>
          </div>
        </div>

        <!-- Packages Grid -->
        <div class="packages-grid">
          
          <!-- Package 1: Base System -->
          <div class="package-card">
            <span class="package-system-type">Base System</span>
            <h3 class="package-title">Full Broadcast Vinyl Flakes</h3>
            <p class="package-desc">
              Heavy-duty anti-slip vinyl flake matrix over 100% solid epoxy primer. Hot-tire pick up proof with an R11 slip rating.
            </p>
            
            <div class="package-price-wrap">
              <span class="package-price-label">Starting from</span>
              <span class="package-price" id="price-vinyl">$1,650</span>
            </div>

            <!-- Single / Double / Triple Car Selector -->
            <div class="garage-options-list" id="opts-vinyl">
              <div class="option-item selected" data-price="$1,650">
                <span>Single Car Garage (up to 24m²)</span>
                <span class="option-check">✓</span>
              </div>
              <div class="option-item" data-price="$2,450">
                <span>Double Car Garage (up to 42m²)</span>
                <span class="option-check">✓</span>
              </div>
              <div class="option-item" data-price="$3,250">
                <span>Triple Car Garage (up to 65m²)</span>
                <span class="option-check">✓</span>
              </div>
            </div>

            <a href="about.html#contact" class="btn btn-outline-teal package-cta" style="text-align:center;">Select Vinyl Flakes</a>
          </div>

          <!-- Package 2: Luxury System -->
          <div class="package-card">
            <span class="package-badge">Premium Finish</span>
            <span class="package-system-type">Luxury System</span>
            <h3 class="package-title">Hybrid Granite Stone Flakes</h3>
            <p class="package-desc">
              Natural micro-granite flake matrix designed to replicate polished terrazzo stone. Scratch-resistant clear shield coat.
            </p>
            
            <div class="package-price-wrap">
              <span class="package-price-label">Starting from</span>
              <span class="package-price" id="price-stone">$1,950</span>
            </div>

            <!-- Single / Double / Triple Car Selector -->
            <div class="garage-options-list" id="opts-stone">
              <div class="option-item selected" data-price="$1,950">
                <span>Single Car Garage (up to 24m²)</span>
                <span class="option-check" style="color:var(--color-gold);">★</span>
              </div>
              <div class="option-item" data-price="$2,850">
                <span>Double Car Garage (up to 42m²)</span>
                <span class="option-check" style="color:var(--color-gold);">★</span>
              </div>
              <div class="option-item" data-price="$3,750">
                <span>Triple Car Garage (up to 65m²)</span>
                <span class="option-check" style="color:var(--color-gold);">★</span>
              </div>
            </div>

            <a href="about.html#contact" class="btn btn-teal package-cta" style="text-align:center;">Select Hybrid Stone</a>
          </div>

        </div>

      </div>
    </section>
""" + footer_template


# services.html
services_content = head_template.format(
    title="Rapid Epoxy — Our Services", 
    description="Comprehensive epoxy and flooring services including concrete grinding, plain epoxy, flakes coating, metallic resin, and specialized sealing."
) + header_template + """
    <!-- ═══════════════════════════════════════
         OUR SERVICES GRID
    ═══════════════════════════════════════ -->
    <section class="section-services" id="services" style="padding-top: var(--space-20);">
      <div class="container">
        
        <div class="services-top-bar">
          <div>
            <span class="eyebrow">PROFESSIONAL COATINGS</span>
            <h1 class="section-title">Specialist Flooring Systems &amp; Services</h1>
            <p class="section-desc">
              Every job begins with mechanical diamond preparation. We install chemical-resistant coatings for garages, retail spaces, factories, shops, cafes, and restaurants.
            </p>
          </div>
          <a href="about.html#contact" class="btn btn-teal">
            Book Site Visit <span style="font-size:1.1rem; line-height:1;">→</span>
          </a>
        </div>

        <!-- 6 Services Grid with Vector SVG Icons -->
        <div class="services-grid">
          
          <!-- Card 1 -->
          <div class="service-card">
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
            </div>
            <h3 class="service-card-title">Plain Epoxy Coating</h3>
            <p class="service-card-desc">
              High-gloss seamless finish available in standard N23 neutral grey, jet black, or custom RAL shades. Hot-tire resistant.
            </p>
            <div class="service-thumb-wrap">
              <img src="img/plain_epoxy.jpg" alt="Plain Epoxy Garage Floor" class="service-thumb">
            </div>
          </div>

          <!-- Card 2 -->
          <div class="service-card">
            <span class="service-badge">From $45/m²</span>
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <h3 class="service-card-title">Epoxy Flakes Coating</h3>
            <p class="service-card-desc">
              Full broadcast vinyl chip floor system. Ideal for residential garages, workshops, and high-foot-traffic utility rooms.
            </p>
            <div class="service-thumb-wrap">
              <img src="img/flake_epoxy.jpg" alt="Epoxy Flakes Texture Floor" class="service-thumb">
            </div>
          </div>

          <!-- Card 3 -->
          <div class="service-card">
            <span class="service-badge">From $90/m²</span>
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            </div>
            <h3 class="service-card-title">Metallic Resin Coating</h3>
            <p class="service-card-desc">
              Seamless 3D metallic liquid marble effect. Hand-manipulated metallic pigments sealed in clear optical-grade resin.
            </p>
            <div class="service-thumb-wrap">
              <img src="img/metallic_epoxy.jpg" alt="Metallic Resin Interior Floor" class="service-thumb">
            </div>
          </div>

          <!-- Card 4 -->
          <div class="service-card">
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><path d="M12 22C6.5 22 2 17.5 2 12S6.5 2 12 2s10 4.5 10 10-4.5 10-10 10zM12 6v6l4 2"/></svg>
            </div>
            <h3 class="service-card-title">Concrete Coloured Sealing</h3>
            <p class="service-card-desc">
              Penetrating UV-stable acrylic sealers with tint capabilities for exposed aggregate, plain concrete, and outdoor areas.
            </p>
          </div>

          <!-- Card 5 -->
          <div class="service-card">
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <h3 class="service-card-title">Driveway &amp; Pergola Sealing</h3>
            <p class="service-card-desc">
              High-pressure wash and solvent sealer application that restores color and blocks oil, salt, and weed penetration.
            </p>
          </div>

          <!-- Card 6 -->
          <div class="service-card">
            <div class="service-icon-box">
              <svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <h3 class="service-card-title">All Types of Floor Coatings</h3>
            <p class="service-card-desc">
              Heavy-duty high-build epoxy designed for shops, cafes, restaurants, factories, and warehouses.
            </p>
            <ul class="service-checklist">
              <li>HACCP Antimicrobial Compliant</li>
              <li>Chemical &amp; Oil Resistant</li>
              <li>Rapid 24-Hour Return to Traffic</li>
            </ul>
          </div>

        </div>

      </div>
    </section>

    <!-- ═══════════════════════════════════════
         DARK TEAL PREP & OTHER SERVICES
    ═══════════════════════════════════════ -->
    <section class="section-prep" id="prep">
      <div class="container">
        
        <div class="prep-container">
          
          <!-- Left: Copy & 3 Sub-Items -->
          <div>
            <span class="eyebrow prep-eyebrow">Other Services &amp; Prep</span>
            <h2 class="prep-title">Concrete Grinding, Leveling &amp; Resurfacing</h2>
            <p class="prep-desc">
              Proper preparation is everything. We use heavy planetary diamond grinders with HEPA dust extractors to open the concrete pores. This guarantees a mechanical bond that will never delaminate. We also offer comprehensive floor leveling and concrete resurfacing.
            </p>

            <div class="prep-list">
              
              <!-- Item 1 -->
              <div class="prep-item">
                <div class="prep-item-num">01</div>
                <div>
                  <h3 class="prep-item-title">Planetary Concrete Grinding</h3>
                  <p class="prep-item-desc">Removes existing paints, latencies, and oils while establishing a rough anchor profile for key adhesion.</p>
                </div>
              </div>

              <!-- Item 2 -->
              <div class="prep-item">
                <div class="prep-item-num">02</div>
                <div>
                  <h3 class="prep-item-title">Floor Leveling &amp; Repair</h3>
                  <p class="prep-item-desc">Cracks, spalls, and uneven floors are repaired and leveled with high-strength rapid curing compounds.</p>
                </div>
              </div>

              <!-- Item 3 -->
              <div class="prep-item">
                <div class="prep-item-num">03</div>
                <div>
                  <h3 class="prep-item-title">Concrete Resurfacing</h3>
                  <p class="prep-item-desc">Complete resurfacing for old, worn-out slabs, giving them a fresh, highly durable new lease on life.</p>
                </div>
              </div>

            </div>
          </div>

          <!-- Right: Concrete Grinding Media -->
          <div class="prep-media-wrap">
            <img src="img/concrete_grinding.jpg" alt="Contractor operating floor grinder machine" class="prep-media-img">
          </div>

        </div>

      </div>
    </section>
""" + footer_template

# about.html
about_content = head_template.format(
    title="Rapid Epoxy — About & Contact", 
    description="Learn about the team behind Rapid Epoxy and get a fixed quote for your flooring project."
) + header_template + """
    <!-- ═══════════════════════════════════════
         FOUNDER STORY / ABOUT OWNER
    ═══════════════════════════════════════ -->
    <section class="section-owner" id="owner" style="padding-top: var(--space-20);">
      <div class="container owner-grid">
        
        <!-- Left: Image & Badge -->
        <div class="owner-image-col">
          <div class="owner-img-wrap">
            <img src="img/owner.jpg" alt="Rapid Epoxy Founder Portrait" class="owner-img">
          </div>

          <div class="experience-badge">
            <div class="exp-icon">
              <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <div class="exp-text">
              <span class="exp-years">10+ Years Trade</span>
              <span class="exp-label">Licensed Installers</span>
            </div>
          </div>
        </div>

        <!-- Right: Story -->
        <div class="owner-content-col">
          <span class="eyebrow">Local Trade Expertise</span>
          <h1 class="owner-title">Direct Owner Supervision On Every Slab.</h1>
          
          <p class="owner-story-text">
            We don't subcontract work to third-party crews. Our own trained 6-man team completes every diamond grind, repair, and topcoat pour using commercial-grade 100% solid resins.<br><br>
            By controlling every stage from moisture testing to final polyaspartic clear coat, we guarantee your garage or commercial floor will look flawless and resist peeling, fading, or chipping for over a decade.
          </p>

          <div class="quote-box">
            &ldquo;Zero shortcuts in prep. 100% solid resin. Guaranteed for 10 years.&rdquo;
          </div>
        </div>

      </div>
    </section>

    <!-- ═══════════════════════════════════════
         GET IN TOUCH & CONTACT FORM
    ═══════════════════════════════════════ -->
    <section class="section-contact" id="contact" style="background:var(--color-surface-sub);">
      <div class="container">
        
        <div class="contact-header">
          <span class="eyebrow">Get in Touch</span>
          <h2 class="section-title">Request Your Fixed Price Quote</h2>
          <p class="section-desc" style="margin: 0 auto;">
            Speak directly with our head installer. We offer free on-site moisture testing and slab inspections across Melbourne &amp; regional Victoria.
          </p>
        </div>

        <div class="contact-grid">
          
          <!-- Direct Contact Card -->
          <div class="direct-contact-card" style="background:var(--color-surface); padding:var(--space-8); border-radius:var(--radius-lg); box-shadow:var(--shadow-card);">
            <h3 class="contact-card-title">Direct Contact</h3>

            <div class="contact-item-list">
              
              <div class="contact-item">
                <div class="contact-item-icon">
                  <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                </div>
                <div>
                  <div class="contact-item-label">Direct Phone</div>
                  <div class="contact-item-val">+61 3 9000 4821</div>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-item-icon">
                  <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                </div>
                <div>
                  <div class="contact-item-label">Email</div>
                  <div class="contact-item-val">quotes@rapidepoxy.com.au</div>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-item-icon">
                  <svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                </div>
                <div>
                  <div class="contact-item-label">Service Region</div>
                  <div class="contact-item-val">Melbourne Metro · Geelong · Mornington Peninsula</div>
                </div>
              </div>

            </div>

            <!-- Map / Visual Placeholder Box -->
            <div style="width:100%; height:140px; background:var(--color-base); border-radius:var(--radius-sm); margin-top:var(--space-8); display:flex; align-items:center; justify-content:center; color:var(--color-muted); font-size:var(--text-xs); font-weight:700; border:1px dashed var(--color-border);">
              <span>📍 On-Site Inspections Daily Across Victoria</span>
            </div>
          </div>

          <!-- Send an Inquiry Form -->
          <div class="inquiry-form-card" style="background:var(--color-surface); padding:var(--space-8); border-radius:var(--radius-lg); box-shadow:var(--shadow-card);">
            <h3 class="contact-card-title" style="margin-bottom:var(--space-6);">Send an Inquiry</h3>

            <form id="inquiryForm" onsubmit="handleFormSubmit(event)">
              
              <div class="form-grid-row">
                <div class="form-group">
                  <label class="form-label" for="fullName">Full Name</label>
                  <input type="text" id="fullName" class="form-input" placeholder="e.g. David Miller" required>
                </div>

                <div class="form-group">
                  <label class="form-label" for="phoneNumber">Phone Number</label>
                  <input type="tel" id="phoneNumber" class="form-input" placeholder="0400 000 000" required>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="serviceType">Flooring System</label>
                <select id="serviceType" class="form-select" required>
                  <option value="Full Broadcast Vinyl Flakes">Full Broadcast Vinyl Flakes</option>
                  <option value="Hybrid Stone Flakes">Hybrid Stone Flakes</option>
                  <option value="3D Metallic Resin">3D Metallic Resin</option>
                  <option value="Solid Plain Industrial Epoxy">Solid Plain Industrial Epoxy</option>
                  <option value="Commercial Factory Flooring">Commercial Factory Flooring</option>
                  <option value="Concrete Sealing & Resurfacing">Concrete Sealing &amp; Resurfacing</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label" for="projectDetails">Approx. Size &amp; Location</label>
                <textarea id="projectDetails" class="form-textarea" placeholder="e.g. Double car garage (approx 36 sqm) in Brighton. Current slab is plain unsealed concrete..." required></textarea>
              </div>

              <!-- Form Action Buttons -->
              <div class="form-actions-row">
                <!-- Green WhatsApp redirect CTA -->
                <button type="button" class="btn btn-whatsapp" onclick="sendViaWhatsApp()" style="flex:1;">
                  <span>Inquire via WhatsApp</span>
                </button>
                
                <span style="font-size:var(--text-xs); color:var(--color-muted);">or</span>

                <button type="submit" class="btn btn-teal" style="flex:1;">
                  <span>Submit Inquiry →</span>
                </button>
              </div>

            </form>
          </div>

        </div>

      </div>
    </section>
""" + footer_template

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)
with open("products.html", "w", encoding="utf-8") as f:
    f.write(products_content)
with open("services.html", "w", encoding="utf-8") as f:
    f.write(services_content)
with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_content)
