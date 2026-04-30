import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract parts
head_match = re.search(r'(<html.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else ''

nav_match = re.search(r'(<!-- ===== NAVBAR ===== -->.*?</nav>)', html, re.DOTALL)
nav_original = nav_match.group(1) if nav_match else ''

footer_match = re.search(r'(<!-- ===== FOOTER ===== -->.*?</html>)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

# Sections
hero_match = re.search(r'(<!-- ===== HERO ===== -->.*?</section>)', html, re.DOTALL)
hero = hero_match.group(1) if hero_match else ''

about_match = re.search(r'(<!-- ===== ABOUT ===== -->.*?</section>)', html, re.DOTALL)
about = about_match.group(1) if about_match else ''

platform_match = re.search(r'(<!-- ===== PLATFORM ===== -->.*?</section>)', html, re.DOTALL)
platform = platform_match.group(1) if platform_match else ''

how_match = re.search(r'(<!-- ===== HOW IT WORKS ===== -->.*?</section>)', html, re.DOTALL)
how = how_match.group(1) if how_match else ''

solutions_match = re.search(r'(<!-- ===== SOLUTIONS ===== -->.*?</section>)', html, re.DOTALL)
solutions = solutions_match.group(1) if solutions_match else ''

usecases_match = re.search(r'(<!-- ===== USE CASES ===== -->.*?</section>)', html, re.DOTALL)
usecases = usecases_match.group(1) if usecases_match else ''

impact_match = re.search(r'(<!-- ===== IMPACT ===== -->.*?</section>)', html, re.DOTALL)
impact = impact_match.group(1) if impact_match else ''

team_match = re.search(r'(<!-- ===== TEAM ===== -->.*?</section>)', html, re.DOTALL)
team = team_match.group(1) if team_match else ''

contact_match = re.search(r'(<!-- ===== CONTACT ===== -->.*?</section>)', html, re.DOTALL)
contact = contact_match.group(1) if contact_match else ''

# Photo breaks
photo_solar_match = re.search(r'(<!-- ===== PHOTO BREAK: SOLAR FARM ===== -->.*?</section>)', html, re.DOTALL)
photo_solar = photo_solar_match.group(1) if photo_solar_match else ''

photo_grid_match = re.search(r'(<!-- ===== PHOTO BREAK: POWER GRID ===== -->.*?</section>)', html, re.DOTALL)
photo_grid = photo_grid_match.group(1) if photo_grid_match else ''

photo_wind_match = re.search(r'(<!-- ===== PHOTO BREAK: WIND FARM ===== -->.*?</section>)', html, re.DOTALL)
photo_wind = photo_wind_match.group(1) if photo_wind_match else ''

photo_earth_match = re.search(r'(<!-- ===== PHOTO BREAK: EARTH ORBIT ===== -->.*?</section>)', html, re.DOTALL)
photo_earth = photo_earth_match.group(1) if photo_earth_match else ''

photo_ai_match = re.search(r'(<!-- ===== PHOTO BREAK: AI DASHBOARD ===== -->.*?</section>)', html, re.DOTALL)
photo_ai = photo_ai_match.group(1) if photo_ai_match else ''

# New Navbar links
new_nav_links = """      <div class="nav-links" id="navLinks">
        <a href="index.html" class="nav-link">Home</a>
        <a href="platform.html" class="nav-link">Platform</a>
        <a href="solutions.html" class="nav-link">Solutions</a>
        <a href="about.html" class="nav-link">About</a>
        <a href="careers.html" class="nav-link">Careers</a>
        <a href="about.html#contact" class="nav-link nav-link-cta">Get in Touch</a>
      </div>"""

new_nav = re.sub(r'<div class="nav-links" id="navLinks">.*?</div>', new_nav_links, nav_original, flags=re.DOTALL)
new_nav = new_nav.replace('href="#"', 'href="index.html"')

# Also update footer links
new_footer_links = """        <div class="footer-links">
          <div class="footer-col">
            <h5>Company</h5>
            <a href="about.html">About</a>
            <a href="about.html#team">Team</a>
            <a href="careers.html">Careers</a>
            <a href="about.html#contact">Contact</a>
          </div>
          <div class="footer-col">
            <h5>Platform</h5>
            <a href="platform.html">Technology</a>
            <a href="solutions.html">Solutions</a>
            <a href="platform.html#how-it-works">How It Works</a>
            <a href="solutions.html#use-cases">Use Cases</a>
          </div>
        </div>"""
new_footer = re.sub(r'<div class="footer-links">.*?</div>\s*</div>', new_footer_links + '\n      </div>', footer, flags=re.DOTALL)
new_footer = new_footer.replace('href="#"', 'href="index.html"')

# Careers Section HTML
careers = """  <!-- ===== CAREERS ===== -->
  <section class="section section-careers" id="careers" style="padding-top: 100px; min-height: 80vh;">
    <div class="container">
      <div class="section-label">Careers</div>
      <h2 class="section-title typed" data-original-html="Join the mission to&lt;br&gt;power the future.">Join the mission to<br>power the future.<span class="typewriter-cursor"></span></h2>
      <p class="section-desc">We are always looking for passionate engineers, scientists, and problem solvers to join our team.</p>
      
      <div class="careers-grid" style="display: grid; grid-template-columns: 1fr; gap: 24px; margin-top: 40px;">
        <div class="career-card" style="padding: 32px; border: 1px solid var(--grey-200); border-radius: 16px; background: var(--white); transition: all 0.3s ease;">
          <h3 style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 600; color: var(--grey-800); margin-bottom: 8px;">Senior Machine Learning Engineer</h3>
          <p style="color: var(--grey-500); margin-bottom: 16px;">Remote / New Delhi • Full-time</p>
          <a href="mailto:careers@biosky.tech" class="btn btn-secondary">Apply Now</a>
        </div>
        <div class="career-card" style="padding: 32px; border: 1px solid var(--grey-200); border-radius: 16px; background: var(--white); transition: all 0.3s ease;">
          <h3 style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 600; color: var(--grey-800); margin-bottom: 8px;">Frontend Developer (React/Next.js)</h3>
          <p style="color: var(--grey-500); margin-bottom: 16px;">New Delhi • Full-time</p>
          <a href="mailto:careers@biosky.tech" class="btn btn-secondary">Apply Now</a>
        </div>
        <div class="career-card" style="padding: 32px; border: 1px solid var(--grey-200); border-radius: 16px; background: var(--white); transition: all 0.3s ease;">
          <h3 style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 600; color: var(--grey-800); margin-bottom: 8px;">Remote Sensing Data Scientist</h3>
          <p style="color: var(--grey-500); margin-bottom: 16px;">Remote / New Delhi • Full-time</p>
          <a href="mailto:careers@biosky.tech" class="btn btn-secondary">Apply Now</a>
        </div>
      </div>
    </div>
  </section>"""

def build_page(title, content):
    page_head = head.replace('<title>BioSky — Space-Powered Energy Intelligence</title>', f'<title>BioSky — {title}</title>')
    return f"{page_head}\n<body style=\"\">\n{new_nav}\n{content}\n{new_footer}"

# Index (Home)
index_content = f"{hero}\n{about}\n{photo_solar}\n{solutions}\n"
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(build_page('Space-Powered Energy Intelligence', index_content))

# Platform
spacer = '<div style="height: var(--nav-height); background: var(--white);"></div>'
platform_content = f"{spacer}\n{platform}\n{photo_grid}\n{how}\n{photo_ai}"
with open('platform.html', 'w', encoding='utf-8') as f:
    f.write(build_page('Platform & Technology', platform_content))

# Solutions
solutions_content = f"{spacer}\n{solutions}\n{photo_wind}\n{usecases}\n{photo_earth}"
with open('solutions.html', 'w', encoding='utf-8') as f:
    f.write(build_page('Solutions', solutions_content))

# About
about_content = f"{spacer}\n{about}\n{impact}\n{team}\n{contact}"
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(build_page('About Us', about_content))

# Careers
careers_content = f"{spacer}\n{careers}"
with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(build_page('Careers', careers_content))

# Update script.js for MPA active links
with open('script.js', 'r', encoding='utf-8') as f:
    script_js = f.read()

# Replace active section highlight
old_active_script = """/* === ACTIVE SECTION HIGHLIGHT ON NAV === */
(function() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const top = section.offsetTop - 150;
      if (window.scrollY >= top) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  });
})();"""

new_active_script = """/* === ACTIVE NAV LINK HIGHLIGHT FOR MPA === */
(function() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.includes(currentPath) && !href.includes('#')) {
      link.classList.add('active');
    }
  });
})();"""

script_js = script_js.replace(old_active_script, new_active_script)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script_js)

print("Refactoring complete.")
