/* ========================================
   BioSky — Interactive JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initHeroParticles();
  initRevealAnimations();
  initTypewriterHeadings();
  initCounterAnimations();
  initMetricBars();
  initSmoothScroll();
  initContactForm();
  initParallaxScroll();
});

/* === NAVBAR === */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  // Scroll behavior
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    lastScroll = scrollY;
  });

  // Mobile toggle
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('active');
    document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
  });

  // Close mobile menu on link click
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
}

/* === HERO PARTICLES — Floating Stars + Shooting Stars === */
function initHeroParticles() {
  const canvas = document.getElementById('heroParticles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width, height, stars, shootingStars;

  function resize() {
    width = canvas.width = canvas.offsetWidth;
    height = canvas.height = canvas.offsetHeight;
  }

  function createStars() {
    stars = [];
    const count = Math.min(120, Math.floor(width * height / 8000));
    for (let i = 0; i < count; i++) {
      stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 1.8 + 0.3,
        baseOpacity: Math.random() * 0.5 + 0.1,
        twinkleSpeed: Math.random() * 0.02 + 0.005,
        twinklePhase: Math.random() * Math.PI * 2,
      });
    }
    shootingStars = [];
  }

  function spawnShootingStar() {
    if (shootingStars.length < 2 && Math.random() < 0.008) {
      shootingStars.push({
        x: Math.random() * width * 0.6,
        y: Math.random() * height * 0.4,
        vx: 4 + Math.random() * 4,
        vy: 2 + Math.random() * 2,
        life: 1,
        decay: 0.015 + Math.random() * 0.01,
        length: 40 + Math.random() * 60,
      });
    }
  }

  function draw(time) {
    ctx.clearRect(0, 0, width, height);

    // Draw twinkling stars
    stars.forEach(s => {
      const twinkle = Math.sin(time * s.twinkleSpeed + s.twinklePhase);
      const opacity = s.baseOpacity + twinkle * 0.25;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(28, 192, 175, ${Math.max(0, opacity)})`;
      ctx.fill();

      // Cross-shaped sparkle for brighter stars
      if (s.radius > 1.2) {
        const sparkleSize = s.radius * 2.5 * (0.5 + twinkle * 0.5);
        ctx.strokeStyle = `rgba(28, 192, 175, ${Math.max(0, opacity * 0.4)})`;
        ctx.lineWidth = 0.5;
        ctx.beginPath();
        ctx.moveTo(s.x - sparkleSize, s.y);
        ctx.lineTo(s.x + sparkleSize, s.y);
        ctx.moveTo(s.x, s.y - sparkleSize);
        ctx.lineTo(s.x, s.y + sparkleSize);
        ctx.stroke();
      }
    });

    // Draw shooting stars
    spawnShootingStar();
    shootingStars = shootingStars.filter(ss => {
      ss.x += ss.vx;
      ss.y += ss.vy;
      ss.life -= ss.decay;

      if (ss.life <= 0) return false;

      const grad = ctx.createLinearGradient(
        ss.x, ss.y,
        ss.x - ss.vx * (ss.length / ss.vx), ss.y - ss.vy * (ss.length / ss.vy)
      );
      grad.addColorStop(0, `rgba(28, 192, 175, ${ss.life * 0.8})`);
      grad.addColorStop(1, `rgba(28, 192, 175, 0)`);

      ctx.beginPath();
      ctx.moveTo(ss.x, ss.y);
      ctx.lineTo(ss.x - ss.vx * (ss.length / ss.vx), ss.y - ss.vy * (ss.length / ss.vy));
      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Bright head
      ctx.beginPath();
      ctx.arc(ss.x, ss.y, 2, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 255, 255, ${ss.life})`;
      ctx.fill();

      return true;
    });

    requestAnimationFrame(draw);
  }

  resize();
  createStars();
  draw(0);

  window.addEventListener('resize', () => {
    resize();
    createStars();
  });
}

/* === PARALLAX SCROLL FOR PHOTO BREAKS === */
function initParallaxScroll() {
  const photoBreaks = document.querySelectorAll('.photo-break-bg');
  
  window.addEventListener('scroll', () => {
    photoBreaks.forEach(bg => {
      const rect = bg.parentElement.getBoundingClientRect();
      const scrollProgress = rect.top / window.innerHeight;
      const yOffset = scrollProgress * -60;
      bg.style.transform = `translateY(${yOffset}px) scale(1.05)`;
    });
  }, { passive: true });
}

/* === REVEAL ON SCROLL === */
function initRevealAnimations() {
  const items = document.querySelectorAll('.reveal-item');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // Stagger delay based on sibling position
          const siblings = entry.target.parentElement.querySelectorAll('.reveal-item');
          const index = Array.from(siblings).indexOf(entry.target);
          setTimeout(() => {
            entry.target.classList.add('revealed');
          }, index * 120);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -60px 0px' }
  );

  items.forEach(item => observer.observe(item));
}

/* === TYPEWRITER HEADINGS === */
function initTypewriterHeadings() {
  const titles = document.querySelectorAll('.section-title');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('typed')) {
          entry.target.classList.add('typed');
          typeWriterEffect(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2, rootMargin: '0px 0px -50px 0px' }
  );

  titles.forEach(title => {
    // Save original HTML and clear for typing
    const html = title.innerHTML.trim();
    title.setAttribute('data-original-html', html);
    title.innerHTML = '&nbsp;'; 
    observer.observe(title);
  });
}

function typeWriterEffect(element) {
  const html = element.getAttribute('data-original-html');
  element.innerHTML = '';
  
  let i = 0;
  let isTag = false;
  let text = '';
  const cursorHTML = '<span class="typewriter-cursor"></span>';
  
  function type() {
    if (i < html.length) {
      if (html.charAt(i) === '<') isTag = true;
      text += html.charAt(i);
      if (html.charAt(i) === '>') isTag = false;
      
      element.innerHTML = text + cursorHTML;
      i++;
      
      const speed = isTag ? 0 : Math.random() * 30 + 15;
      setTimeout(type, speed);
    } else {
      element.innerHTML = text + cursorHTML;
    }
  }
  type();
}

/* === COUNTER ANIMATION === */
function initCounterAnimations() {
  const counters = document.querySelectorAll('.metric-value[data-target]');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  counters.forEach(counter => observer.observe(counter));
}

function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-target'));
  const duration = 2000;
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease-out cubic
    const easeOut = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.round(target * easeOut);
    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

/* === METRIC BARS === */
function initMetricBars() {
  const fills = document.querySelectorAll('.metric-fill');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.classList.add('animate');
          }, 500);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  fills.forEach(fill => observer.observe(fill));
}

/* === SMOOTH SCROLL === */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href === '#') return;

      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        const offsetTop = target.offsetTop - 72; // nav height
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
}

/* === CONTACT FORM === */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const btn = document.getElementById('submitBtn');
    const originalText = btn.innerHTML;

    // Simulate submission
    btn.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" class="spin">
        <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" stroke-dasharray="32" stroke-dashoffset="32" stroke-linecap="round">
          <animate attributeName="stroke-dashoffset" from="32" to="0" dur="0.8s" fill="freeze"/>
        </circle>
      </svg>
      Sending...
    `;
    btn.disabled = true;
    btn.style.opacity = '0.7';

    setTimeout(() => {
      btn.innerHTML = `
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M3 8L7 12L13 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Message Sent!
      `;
      btn.style.opacity = '1';
      btn.style.background = '#374151';

      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
        btn.style.background = '';
        form.reset();
      }, 3000);
    }, 1500);
  });

  // Input focus animations
  form.querySelectorAll('input, textarea').forEach(input => {
    input.addEventListener('focus', () => {
      input.parentElement.classList.add('focused');
    });
    input.addEventListener('blur', () => {
      input.parentElement.classList.remove('focused');
    });
  });
}

/* === ACTIVE NAV LINK HIGHLIGHT FOR MPA === */
(function() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.includes(currentPath) && !href.includes('#')) {
      link.classList.add('active');
    }
  });
})();
