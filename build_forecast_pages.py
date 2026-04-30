import re

# ==========================================
# SOLAR FORECASTING CONTENT
# ==========================================
solar_content = """
  <!-- HERO -->
  <section class="about-hero" style="position: relative; min-height: 50vh; display: flex; align-items: center; background: #0b0f19; padding-top: var(--nav-height); overflow: hidden;">
    <div class="about-hero-bg" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('assets/solutions/solar_hero.jpg'); background-size: cover; background-position: center; opacity: 0.4; z-index: 0;"></div>
    <div class="container about-hero-content" style="position: relative; z-index: 2; max-width: 800px; padding: 60px 0 120px 0;">
      <h1 class="about-hero-title" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #fff; margin-bottom: 20px; text-transform: uppercase;">SOLAR FORECASTING</h1>
      <p class="about-hero-subtitle" style="font-size: 1.2rem; color: #e2e8f0; margin-bottom: 30px;">Powering a more stable, low-carbon solar power future</p>
      <a href="about.html#contact" class="btn btn-primary" style="background: transparent; border: 1px solid #fff; color: #fff; padding: 12px 24px; border-radius: 50px; text-decoration: none; font-weight: 500; transition: all 0.3s ease;">Get in touch</a>
    </div>
  </section>

  <!-- INTRO SECTION (DARK) -->
  <section style="background: #000; color: #fff; padding: 80px 0;">
    <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
      <div>
        <h2 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 2rem; margin-bottom: 24px; line-height: 1.3;">High-accuracy solar generation forecasts powered by satellite intelligence & physics-informed AI</h2>
        <p style="color: var(--grey-300); font-size: 1.1rem; line-height: 1.6;">BioSky's Solar Energy Forecasting System brings unmatched accuracy to power producers and grid operators, using space-based intelligence fused with advanced AI models.</p>
      </div>
      <div>
        <div style="width: 100%; height: 300px; background-image: url('assets/solutions/solar_panels_1.jpg'); background-size: cover; background-position: center; border-radius: 200px 200px 0 0; overflow: hidden; position: relative;">
          <!-- Placeholder or add image -->
        </div>
      </div>
    </div>
  </section>

  <!-- WHY CHOOSE US -->
  <section style="background: #000; color: #fff; padding-bottom: 80px;">
    <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
      <div>
        <h3 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 1.8rem; margin-bottom: 20px;">Why choose us?</h3>
        <p style="color: var(--grey-300); font-size: 1.05rem; line-height: 1.6; margin-bottom: 40px;">Built for the unique climatic complexity of India and the Global South, our proprietary framework extracts real-time cloud and irradiance patterns to predict solar generation. BioSky enables utilities & IPPs to deliver more stable, low-carbon solar power - supporting SDG 7 (Clean Energy) and SDG 13 (Climate Action)</p>
        <div style="display: flex; gap: 60px;">
          <div>
             <h4 style="color: var(--accent-cyan); font-size: 1.8rem; font-weight: 700; margin-bottom: 8px;">&lt;8%</h4>
             <p style="color: var(--grey-400); text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em;">RMSE</p>
          </div>
          <div>
             <h4 style="color: var(--accent-cyan); font-size: 1.8rem; font-weight: 700; margin-bottom: 8px;">95%</h4>
             <p style="color: var(--grey-400); text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em;">Forecast Accuracy</p>
          </div>
        </div>
      </div>
      <div>
        <img src="assets/solutions/solar_panels_2.jpg" alt="Solar panels" style="width: 100%; border-radius: 8px;" onerror="this.src='https://via.placeholder.com/600x400/111/333?text=Solar+Panels'">
      </div>
    </div>
  </section>

  <!-- OUR APPROACH -->
  <section style="background: #112529; color: #fff; padding: 80px 0; position: relative; overflow: hidden;">
    <!-- background image with overlay -->
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('assets/solutions/solar_bg.jpg'); background-size: cover; background-position: center; opacity: 0.2;"></div>
    <div class="container" style="position: relative; z-index: 2;">
      <h3 style="font-family: var(--font-display); font-size: 2rem; margin-bottom: 40px;">Our approach</h3>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
        <div style="background: var(--accent-cyan); color: #000; padding: 40px 30px; border-radius: 4px;">
           <h4 style="font-size: 1.3rem; margin-bottom: 24px; font-weight: 600;">Data Ingestion</h4>
           <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6; font-size: 0.95rem;">
             <li>Multi-sensor satellite imagery (optical, IR, radar)</li>
             <li>Weather API & ground sensors</li>
           </ul>
        </div>
        <div style="background: var(--accent-cyan); color: #000; padding: 40px 30px; border-radius: 4px;">
           <h4 style="font-size: 1.3rem; margin-bottom: 24px; font-weight: 600;">AI Processing</h4>
           <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6; font-size: 0.95rem;">
             <li>Physics-informed AI</li>
             <li>Cloud tracking & motion vectors</li>
             <li>Irradiance attenuation modeling</li>
           </ul>
        </div>
        <div style="background: var(--accent-cyan); color: #000; padding: 40px 30px; border-radius: 4px;">
           <h4 style="font-size: 1.3rem; margin-bottom: 24px; font-weight: 600;">Forecast Output</h4>
           <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6; font-size: 0.95rem;">
             <li>Sub-hourly GHI, DNI</li>
             <li>PV power forecasts (plant-level)</li>
           </ul>
        </div>
      </div>
      
      <div style="margin-top: 60px;">
        <h3 style="font-family: var(--font-display); font-size: 1.8rem; margin-bottom: 30px; color: var(--accent-cyan);">Key Features</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 40px;">
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">Hyper-local forecasting down to 10-minute intervals</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">Cloud-motion tracking models for dynamic irradiance prediction</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">Multi-source fusion of satellite, weather, & ground station data</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">Physics-informed AI models for India's monsoon & dust conditions</p>
          </div>
        </div>
        <p style="color: var(--accent-cyan); font-size: 1.1rem; margin-bottom: 30px;">Reduce DSM penalties by up to 40% and improve dispatch efficiency</p>
        <a href="about.html#contact" class="btn btn-primary" style="background: transparent; border: 1px solid #fff; color: #fff; padding: 10px 24px; border-radius: 50px; text-decoration: none; font-size: 0.9rem;">Get in touch</a>
      </div>
    </div>
  </section>

  <!-- REAL WORLD IMPACT -->
  <section style="background: #000; color: #fff; padding: 80px 0; text-align: center; position: relative;">
     <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('assets/solutions/solar_impact.jpg'); background-size: cover; background-position: center; opacity: 0.3;"></div>
     <div class="container" style="position: relative; z-index: 2;">
        <h2 style="color: var(--accent-cyan); font-family: var(--font-display); font-size: 2.5rem; margin-bottom: 16px;">Real world Impact</h2>
        <p style="font-size: 0.9rem; letter-spacing: 0.1em; color: var(--grey-300); margin-bottom: 40px; text-transform: uppercase;">CASE STUDY: SUNPOWER RENEWABLES</p>
        <a href="#" class="btn btn-primary" style="background: #000; border: 1px solid #333; color: #fff; padding: 12px 32px; border-radius: 50px; text-decoration: none; font-size: 0.95rem;">Know More</a>
     </div>
  </section>
"""


# ==========================================
# WIND FORECASTING CONTENT
# ==========================================
wind_content = """
  <!-- HERO -->
  <section class="about-hero" style="position: relative; min-height: 50vh; display: flex; align-items: center; background: #0b0f19; padding-top: var(--nav-height); overflow: hidden;">
    <div class="about-hero-bg" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: url('assets/solutions/wind_hero.jpg'); background-size: cover; background-position: center; opacity: 0.4; z-index: 0;"></div>
    <div class="container about-hero-content" style="position: relative; z-index: 2; max-width: 800px; padding: 60px 0 120px 0;">
      <h1 class="about-hero-title" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #fff; margin-bottom: 20px; text-transform: uppercase;">WIND FORECASTING</h1>
      <p class="about-hero-subtitle" style="font-size: 1.2rem; color: #e2e8f0; margin-bottom: 30px;">Precision forecasts for smarter wind operations</p>
      <a href="about.html#contact" class="btn btn-primary" style="background: transparent; border: 1px solid #fff; color: #fff; padding: 12px 24px; border-radius: 50px; text-decoration: none; font-weight: 500; transition: all 0.3s ease;">Get in Touch</a>
    </div>
  </section>

  <!-- INTRO SECTION (LIGHT) -->
  <section style="background: #fff; color: #000; padding: 80px 0;">
    <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
      <div>
        <h2 style="color: #1A3C40; font-family: var(--font-display); font-size: 2rem; margin-bottom: 24px; line-height: 1.3;">Real-time, AI-enhanced wind generation forecasts with spatial awareness & asset-level precision.</h2>
        <p style="color: var(--grey-600); font-size: 1.1rem; line-height: 1.6;">Using satellite data, SCADA integration, and neural modeling, our system captures site-specific effects - like terrain, thermal stress, and turbulence - achieving forecast accuracy > 90%</p>
      </div>
      <div>
        <img src="assets/solutions/wind_turbines.jpg" alt="Wind Turbines" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" onerror="this.src='https://via.placeholder.com/600x400/ddd/555?text=Wind+Turbines'">
      </div>
    </div>
  </section>

  <!-- WHAT POWERS OUR FORECASTS (DARK) -->
  <section style="background: #000; color: #fff; padding: 80px 0;">
    <div class="container">
      <h2 style="font-family: var(--font-display); font-size: 2rem; margin-bottom: 50px; text-transform: uppercase; text-align: center;">WHAT POWERS OUR FORECASTS</h2>
      
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 60px;">
        <div style="background: var(--accent-cyan); color: #000; padding: 40px 30px; text-align: center; border-radius: 4px;">
           <svg viewBox="0 0 24 24" width="48" height="48" stroke="currentColor" stroke-width="1.5" fill="none" style="margin-bottom: 20px;"><path d="M12 2L2 12l10 10 10-10L12 2z"></path><path d="M2 12h20"></path><path d="M12 2v20"></path></svg>
           <p style="font-size: 0.95rem; line-height: 1.5; font-weight: 500;">We fuse numerical weather prediction (NWP) with satellite and turbine-level SCADA data.</p>
        </div>
        <div style="background: var(--accent-cyan); color: #000; padding: 40px 30px; text-align: center; border-radius: 4px;">
           <svg viewBox="0 0 24 24" width="48" height="48" stroke="currentColor" stroke-width="1.5" fill="none" style="margin-bottom: 20px;"><circle cx="12" cy="12" r="10"></circle><path d="M8 12h8"></path><path d="M12 8v8"></path></svg>
           <p style="font-size: 0.95rem; line-height: 1.5; font-weight: 500;">Our deep learning models continuously adapt to wind ramp rates, turbulence, and wake effects.</p>
        </div>
        <div style="background: var(--accent-cyan); color: #000; padding: 40px 30px; text-align: center; border-radius: 4px;">
           <svg viewBox="0 0 24 24" width="48" height="48" stroke="currentColor" stroke-width="1.5" fill="none" style="margin-bottom: 20px;"><path d="M4 4h16v16H4z"></path><path d="M4 12h16"></path><path d="M12 4v16"></path></svg>
           <p style="font-size: 0.95rem; line-height: 1.5; font-weight: 500;">We produce reliable power forecasts for horizons ranging from 10 minutes to 72 hours.</p>
        </div>
      </div>
      
      <div style="max-width: 900px;">
        <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 30px;">Key Features</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 50px;">
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">Sub-hourly forecasts at 0.5 km spatial resolution</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">AI + physics hybrid modeling tuned to local geography</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">Real-time ramp rate alerts for proactive grid balancing</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">SCADA integration for ongoing model adaptation</p>
          </div>
          <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="width: 8px; height: 8px; background: var(--accent-cyan); margin-top: 8px; flex-shrink: 0;"></div>
            <p style="margin: 0; font-size: 0.95rem;">DSM cost reduction through accurate short-term forecasts</p>
          </div>
        </div>

        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px; color: var(--grey-300);">BioSky's wind forecasting helps utilities, traders & operators stabilize renewable output, prevent imbalance penalties, and ensure grid resilience</p>
        <a href="about.html#contact" class="btn btn-primary" style="background: var(--accent-cyan); color: #000; padding: 12px 32px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block;">Get in Touch</a>
      </div>
    </div>
  </section>
"""

import sys

def inject_content(file_path, content_tag, content):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(f'<!-- {content_tag} -->', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

inject_content('solar-forecasting.html', 'SOLAR CONTENT', solar_content)
inject_content('wind-forecasting.html', 'WIND CONTENT', wind_content)

print("Injected content successfully")
