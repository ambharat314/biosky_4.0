import re

new_html_content = """  <!-- ===== ABOUT HERO ===== -->
  <section class="about-hero" style="position: relative; min-height: 50vh; display: flex; align-items: center; background: #0b0f19; padding-top: var(--nav-height); overflow: hidden;">
    <div class="about-hero-bg" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('assets/earth_orbit.jpg'); background-size: cover; background-position: center; opacity: 0.3; z-index: 0;"></div>
    <div class="container about-hero-content" style="position: relative; z-index: 2; max-width: 800px; text-align: center; margin: 0 auto; padding: 60px 0 120px 0;">
      <h1 class="about-hero-title" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #fff; margin-bottom: 24px;">About BioSky</h1>
      <p class="about-hero-subtitle" style="font-size: 1.1rem; color: var(--grey-300); line-height: 1.7;">BioSky Space Innovations Pvt. Ltd. is a spacetech company using AI and Satellite Imagery to power India's energy resilience.</p>
    </div>
  </section>

  <!-- ===== MISSION & VISION ===== -->
  <section class="about-mission-vision" style="background: var(--white); padding-bottom: 80px;">
    <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: -80px; position: relative; z-index: 10;">
       <div class="mission-box" style="background: #1A3C40; color: white; padding: 60px 40px; border-radius: 8px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
          <h2 style="font-family: var(--font-display); font-size: 2.2rem; margin-bottom: 24px; color: #fff;">Mission</h2>
          <p style="font-size: 1.1rem; line-height: 1.6; color: #E2E8F0;">To build India's first space-powered energy intelligence stack for clean, reliable, and equitable power</p>
       </div>
       <div class="vision-box" style="background: #1A3C40; color: white; padding: 60px 40px; border-radius: 8px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
          <h2 style="font-family: var(--font-display); font-size: 2.2rem; margin-bottom: 24px; color: #fff;">Vision</h2>
          <p style="font-size: 1.1rem; line-height: 1.6; color: #E2E8F0;">Creating a global spacetech leader from India, delivering transformative solutions across critical industries</p>
       </div>
    </div>
  </section>

  <!-- ===== TEAM ===== -->
  <section class="section team-section" style="background: var(--white); padding: 40px 0 80px 0;">
    <div class="container">
      <h2 class="section-title text-center" style="color: #1A3C40; font-size: 2.5rem; margin-bottom: 20px;">Our team</h2>
      <p class="section-desc text-center" style="max-width: 800px; margin: 0 auto 60px auto; color: var(--grey-600);">A world-class group of scientists, engineers, and strategists from IITs, IIMs, and leading research institutes, united by one goal: to apply space technology for planetary resilience.</p>
      
      <!-- Row 1: 5 members -->
      <div style="display: flex; gap: 32px; justify-content: center; margin-bottom: 40px; flex-wrap: wrap;">
        <!-- Saurabh -->
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/saurabh.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Saurabh Kapil</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">CO-FOUNDER AND CEO</p>
          </div>
          <a href="#" style="color: #1E293B; display: inline-block; margin-top: auto;">
             <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </a>
        </div>
        <!-- Nimish -->
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/nimish.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Nimish Nama</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">CO-FOUNDER AND CTO</p>
          </div>
          <a href="#" style="color: #1E293B; display: inline-block; margin-top: auto;">
             <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </a>
        </div>
        <!-- Abhishek -->
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/abhishek.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Abhishek Yadav</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">PRINCIPAL REMOTE SENSING SCIENTIST</p>
          </div>
          <a href="#" style="color: #1E293B; display: inline-block; margin-top: auto;">
             <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </a>
        </div>
        <!-- Archana -->
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/archana.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Archana Yadav</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">ML AND DATA SCIENTIST</p>
          </div>
          <a href="#" style="color: #1E293B; display: inline-block; margin-top: auto;">
             <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </a>
        </div>
        <!-- Hemraj -->
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/hemraj.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Hemraj Chakrawarti</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">ML SCIENTIST</p>
          </div>
          <a href="#" style="color: #1E293B; display: inline-block; margin-top: auto;">
             <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </a>
        </div>
      </div>
      
      <div style="max-width: 1000px; margin: 0 auto;">
         <hr style="border: none; border-top: 1px solid var(--grey-300); margin-bottom: 40px;" />
      </div>

      <!-- Row 2: 2 members -->
      <div style="display: flex; gap: 32px; justify-content: flex-start; margin-bottom: 40px; flex-wrap: wrap; max-width: 1000px; margin: 0 auto;">
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/praveen.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Praveen Kumar</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">SENIOR SOFTWARE ENGINEER</p>
          </div>
        </div>
        <div style="width: 180px; display: flex; flex-direction: column; gap: 12px;">
          <img src="assets/teams/parth.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
          <div>
            <h4 style="font-size: 1.05rem; color: #1E293B; margin: 0 0 4px 0; font-weight: 600;">Parth Sharma</h4>
            <p style="font-size: 0.75rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin: 0; letter-spacing: 0.05em;">FOUNDERS OFFICE</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== RECOGNITIONS ===== -->
  <section class="section recognitions-section" style="background: #F4FAF9; padding: 80px 0;">
    <div class="container">
      <h2 class="section-title text-center" style="color: #1A3C40; margin-bottom: 40px; font-size: 2.5rem;">Recognitions</h2>
      <div class="recognitions-list" style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px;">
"""

recognitions = [
    "Among 2 Indian startups selected for ICC Venture Catalyst Space (Australia) 2024",
    "Among 15 international startups chosen for TAcc+ International SpaceTech Startup, Taiwan 2024",
    "Finalist - TATA Enterprise Challenge",
    "Microsoft (Unnati), AWS Space Accelerator & Climate Collective AI Startup",
    "Youth-led Innovation Award in Climate & AI - United Nations ESCAP, Bangkok (2024)",
    "Among 3 enterprises selected by the UK British High Commission to represent India on grid and energy challenges",
    "Among 10 international startups selected for TAcc+ SpaceTech Program, Taiwan (2023)",
    "Among 3 Indian startups selected for ICC Venture Catalyst Space Program, Australia (2023)",
    "Selected among Top 100 Tech Entrepreneurs - Bharat Innovates, representing India at the Indo-French Summit",
    "Top 15 startups selected in the Microsoft Unnati program",
    "IndiaAI summit representation with Microsoft",
    "Top 10 startups in ReNew Ace Initiative",
    "Finalist - TATA Enterprise Challenge",
    "Part of the FIICCI-C-CAMP, IIT Madras",
    "US-India AI Collaborative Innovation Programme"
]

for rec in recognitions:
    new_html_content += f"""
         <div style="display: flex; gap: 16px; align-items: flex-start;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent-blue); width: 20px; height: 20px; flex-shrink: 0; margin-top: 2px;">
               <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
               <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <p style="margin: 0; color: #334155; font-size: 1rem; line-height: 1.5;">{rec}</p>
         </div>"""

new_html_content += """
      </div>
    </div>
  </section>

  <!-- ===== PARTNERSHIPS ===== -->
  <section class="section partners-section" style="background: #F4FAF9; padding-bottom: 100px;">
    <div class="container" style="max-width: 900px; margin: 0 auto; text-align: center;">
      
      <h3 style="color: #1A3C40; font-size: 1.8rem; margin-bottom: 24px; font-family: var(--font-display); font-weight: 600;">Research Partnerships & Collaborations</h3>
      <div style="background: white; padding: 40px; border-radius: 12px; display: flex; justify-content: space-around; align-items: center; margin-bottom: 60px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); flex-wrap: wrap; gap: 20px;">
        <span style="font-weight: 700; font-size: 1.1rem; color: #334155;">Govt of India (DST)</span>
        <span style="font-weight: 700; font-size: 1.1rem; color: #334155;">Adelaide University</span>
        <span style="font-weight: 700; font-size: 1.1rem; color: #334155;">ICC</span>
        <span style="font-weight: 700; font-size: 1.1rem; color: #334155;">University of South Australia</span>
      </div>

      <h3 style="color: #1A3C40; font-size: 1.8rem; margin-bottom: 24px; font-family: var(--font-display); font-weight: 600;">Technology Support</h3>
      <div style="background: white; padding: 40px; border-radius: 12px; display: flex; justify-content: center; gap: 60px; align-items: center; margin-bottom: 60px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); flex-wrap: wrap;">
        <span style="font-weight: 800; font-size: 2rem; color: #00A4EF; letter-spacing: -0.02em;">Microsoft</span>
        <span style="font-weight: 800; font-size: 2rem; color: #FF9900; letter-spacing: -0.05em;">aws</span>
        <span style="font-weight: 800; font-size: 1.8rem; color: #76B900;">NVIDIA<br><span style="font-size: 0.8rem; letter-spacing: 0.1em; font-weight: 600; color: #333; display: block; margin-top: -5px;">INCEPTION PROGRAM</span></span>
      </div>

      <h3 style="color: #1A3C40; font-size: 1.8rem; margin-bottom: 24px; font-family: var(--font-display); font-weight: 600;">Investment and Grants</h3>
      <div style="background: white; padding: 50px; border-radius: 12px; display: flex; flex-direction: column; gap: 40px; align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <div style="display: flex; justify-content: center; gap: 50px; align-items: center; flex-wrap: wrap;">
           <span style="font-weight: 700; font-size: 1.5rem; color: #005F9E;">sidbi</span>
           <span style="font-weight: 700; font-size: 1.2rem; color: #334155; max-width: 150px; line-height: 1.2;">FOUNDATION FOR INNOVATION AND TECHNOLOGY TRANSFER</span>
           <span style="font-weight: 800; font-size: 1.5rem; color: #334155;">Unnati.ai</span>
           <span style="font-weight: 700; font-size: 1.2rem; color: #C00;">IIT Delhi</span>
        </div>
        <div style="display: flex; justify-content: center; gap: 50px; align-items: center; flex-wrap: wrap;">
           <span style="font-weight: 700; font-size: 1.1rem; color: #334155; max-width: 200px; line-height: 1.2;">Govt of India<br>Ministry of Electronics and Information Technology</span>
           <span style="font-weight: 800; font-size: 1.5rem; color: #334155;">ICC <span style="font-weight: 600; font-size: 0.9rem; margin-left: 8px;">INNOVATION &<br>COLLABORATION CENTRE</span></span>
        </div>
      </div>
    </div>
  </section>
"""

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

nav_end_idx = html.find('</nav>') + 6

# we want to keep the contact section and footer
contact_start_idx = html.find('<!-- ===== CONTACT ===== -->')

new_page = html[:nav_end_idx] + "\n" + new_html_content + "\n" + html[contact_start_idx:]

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(new_page)

print("About page built successfully.")
