import re

new_html_content = """  <!-- ===== PLATFORM HERO ===== -->
  <section class="platform-hero">
    <div class="platform-hero-bg"></div>
    <div class="container platform-hero-content">
      <div class="platform-hero-header">
        <div class="platform-badge-logo">
          <svg viewBox="0 0 24 24" fill="currentColor">
             <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
          </svg>
          BIOSKY<br>ENERGY STACK
        </div>
      </div>
      <h1 class="platform-hero-title">Space-Powered Intelligence for the Modern Grid</h1>
      <p class="platform-hero-subtitle">India's first decision-intelligence layer - fusing satellites, AI, and grid data to make power reliable and climate-resilient.</p>
      <a href="about.html#contact" class="btn btn-primary" style="background: var(--accent-blue); color: #fff;">Enquire Now</a>
    </div>
  </section>

  <!-- ===== SHIFT SECTION ===== -->
  <section class="section platform-shift">
    <div class="container shift-container">
      <div class="shift-left">
        <h2 class="section-title shift-title">A Space-Powered Shift in Energy Intelligence</h2>
        <p class="shift-desc">BioSky unites multiple Earth observation, AI, and grid analytics to create a living intelligence layer across the energy value chain.</p>
        <p class="shift-desc">Our system fuses multi-sensor data - from optical and radar satellites to weather APIs and grid telemetry - creating a living, adaptive model of the energy ecosystem.</p>
        
        <div class="shift-features">
          <div class="shift-feature">
             <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
             </div>
             <div>
               <h4>Sub-Hourly Forecasting</h4>
               <p>Predict renewable generation at sub-hourly intervals for smarter scheduling and dispatch.</p>
             </div>
          </div>
          <div class="shift-feature">
             <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
             </div>
             <div>
               <h4>Real-Time Grid Awareness</h4>
               <p>Detect voltage fluctuations and stress points as they occur, in real-time.</p>
             </div>
          </div>
          <div class="shift-feature">
             <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
             </div>
             <div>
               <h4>Predictive Resilience</h4>
               <p>Anticipate disruptions from weather, vegetation, or thermal overloads.</p>
             </div>
          </div>
          <div class="shift-feature">
             <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20V10"/><path d="M18 20V4"/><path d="M6 20v-4"/></svg>
             </div>
             <div>
               <h4>Optimized Intelligence</h4>
               <p>Optimize procurement and dispatch for cost and carbon efficiency.</p>
             </div>
          </div>
        </div>
      </div>
      <div class="shift-right">
         <div class="shift-image-wrapper">
            <img src="assets/earth_orbit.jpg" alt="Earth from space" />
            <div class="shift-image-caption">satellite data, power sector intelligence</div>
         </div>
      </div>
    </div>
  </section>

  <!-- ===== DIGITAL TWINS ===== -->
  <section class="section platform-twins">
    <div class="twins-bg"></div>
    <div class="container twins-content">
       <h2 class="section-title text-white twins-title">DIGITAL TWINS FOR GRID RESILIENCE</h2>
       <p class="twins-subtitle">Every region becomes a digital twin - a continuously updated, satellite-informed model that learns from each event. Linked together, these twins let utilities simulate, forecast, and design climate-ready power systems.</p>
       <a href="about.html#contact" class="btn btn-secondary twins-btn">Contact Us</a>
       
       <div class="twins-grid">
         <div class="twin-card">
           <h4>Space-Powered Precision</h4>
           <p>Multi-sensor satellites and grid telemetry for real-time visibility.</p>
         </div>
         <div class="twin-card">
           <h4>Physics-informed AI</h4>
           <p>Models rooted in the physical realities of energy flows.</p>
         </div>
         <div class="twin-card">
           <h4>Multi-horizon Intelligence</h4>
           <p>From sub-hourly operations to long-term planning.</p>
         </div>
         <div class="twin-card">
           <h4>Built for emerging Grids</h4>
           <p>Designed for the climate variability of India and the Global South.</p>
         </div>
       </div>
    </div>
  </section>

  <!-- ===== IMPACT AT SCALE ===== -->
  <section class="section platform-impact">
     <div class="container text-center">
       <h2 class="section-title center impact-main-title">Impact At Scale</h2>
       <p class="section-desc center impact-main-desc">We deliver measurable operational and environmental impact:</p>
       
       <div class="impact-cards-grid">
         <div class="impact-box">
           <div class="impact-value">15-20%</div>
           <p>improvement in demand/load forecast accuracy</p>
         </div>
         <div class="impact-box">
           <div class="impact-value">5-10%</div>
           <p>reduction in power purchase costs</p>
         </div>
         <div class="impact-box">
           <div class="impact-value">1,00,000</div>
           <p>tonnes CO2 savings per year<br>(India scale)</p>
         </div>
         <div class="impact-box">
           <div class="impact-value">8-12%</div>
           <p>renewable utilization and reduced grid curtailment.</p>
         </div>
       </div>
     </div>
  </section>"""

with open('platform.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the content between navbar and footer
nav_end_idx = html.find('</nav>') + 6
footer_start_idx = html.find('<!-- ===== FOOTER ===== -->')

new_page = html[:nav_end_idx] + "\n" + new_html_content + "\n" + html[footer_start_idx:]

with open('platform.html', 'w', encoding='utf-8') as f:
    f.write(new_page)

css_append = """
/* === PLATFORM PAGE STYLES === */
.platform-hero {
  position: relative;
  min-height: 80vh;
  display: flex;
  align-items: center;
  background: var(--off-white);
  padding-top: var(--nav-height);
  overflow: hidden;
}

.platform-hero-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: url('assets/power_grid.jpg');
  background-size: cover;
  background-position: center;
  opacity: 0.15;
  z-index: 0;
}

.platform-hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
}

.platform-hero-header {
  position: absolute;
  top: 40px;
  right: 40px;
  display: flex;
  justify-content: flex-end;
  width: 100%;
}

.platform-badge-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--grey-900);
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: 0.05em;
  text-align: left;
  line-height: 1.2;
}

.platform-badge-logo svg {
  width: 24px; height: 24px;
}

.platform-hero-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  font-weight: 700;
  color: var(--white);
  color: #fff;
  line-height: 1.15;
  margin-bottom: 24px;
  margin-top: 100px;
}

.platform-hero-subtitle {
  font-size: 1.1rem;
  color: var(--grey-400);
  line-height: 1.7;
  max-width: 600px;
  margin-bottom: 40px;
}

.platform-shift {
  background: var(--white);
}

.shift-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.shift-title {
  color: #1A3C40;
  font-size: 2.2rem;
  margin-bottom: 30px;
}

.shift-desc {
  font-size: 1.05rem;
  color: var(--grey-500);
  line-height: 1.7;
  margin-bottom: 24px;
}

.shift-features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-top: 40px;
}

.shift-feature {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.feature-icon {
  width: 48px;
  height: 48px;
  background: rgba(28, 192, 175, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-blue);
}

.feature-icon svg {
  width: 24px;
  height: 24px;
}

.shift-feature h4 {
  color: var(--accent-blue);
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 8px;
  font-family: var(--font-display);
}

.shift-feature p {
  font-size: 0.9rem;
  color: var(--grey-500);
  line-height: 1.6;
}

.shift-image-wrapper {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.shift-image-wrapper img {
  width: 100%;
  height: auto;
  display: block;
}

.shift-image-caption {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(4px);
  color: #fff;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.8rem;
  letter-spacing: 0.05em;
  border: 1px solid rgba(255,255,255,0.1);
}

.platform-twins {
  position: relative;
  background: var(--off-white);
  padding: 100px 0;
  overflow: hidden;
}

.twins-bg {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 150vw; height: 150vw;
  background: radial-gradient(circle, rgba(28,192,175,0.15) 0%, rgba(11,15,25,1) 50%);
  z-index: 0;
  pointer-events: none;
}

.twins-content {
  position: relative;
  z-index: 1;
}

.twins-title {
  text-transform: uppercase;
  color: #fff;
  font-size: 2.2rem;
  letter-spacing: 0.05em;
}

.twins-subtitle {
  color: var(--grey-400);
  font-size: 1.1rem;
  line-height: 1.7;
  max-width: 800px;
  margin-bottom: 40px;
}

.twins-btn {
  border-color: rgba(255,255,255,0.2);
  color: #fff;
  margin-bottom: 80px;
}

.twins-btn:hover {
  background: rgba(255,255,255,0.1);
  border-color: rgba(255,255,255,0.4);
}

.twins-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.twin-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 32px 24px;
  border-radius: 12px;
  backdrop-filter: blur(10px);
}

.twin-card h4 {
  color: var(--accent-blue);
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 12px;
  font-family: var(--font-display);
}

.twin-card p {
  color: var(--grey-400);
  font-size: 0.9rem;
  line-height: 1.6;
}

.platform-impact {
  background: var(--white);
  padding: 100px 0;
}

.impact-main-title {
  color: #1A3C40;
}

.impact-main-desc {
  margin-bottom: 60px;
}

.impact-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  max-width: 800px;
  margin: 0 auto;
}

.impact-box {
  background: #F4FAF9;
  border: 1px solid rgba(28, 192, 175, 0.1);
  padding: 48px 32px;
  border-radius: 12px;
  text-align: center;
}

.impact-box .impact-value {
  color: var(--accent-blue);
  font-size: 2.5rem;
  font-weight: 700;
  font-family: var(--font-display);
  margin-bottom: 12px;
  line-height: 1;
}

.impact-box p {
  color: var(--grey-500);
  font-size: 0.95rem;
  line-height: 1.5;
}

@media (max-width: 1024px) {
  .shift-container {
    grid-template-columns: 1fr;
  }
  
  .twins-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .impact-cards-grid {
    grid-template-columns: 1fr;
  }
  
  .shift-features {
    grid-template-columns: 1fr;
  }
  
  .twins-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Platform page built successfully.")
