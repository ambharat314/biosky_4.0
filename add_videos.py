import re

# Update Solar Forecasting
with open('solar-forecasting.html', 'r', encoding='utf-8') as f:
    solar_html = f.read()

solar_hero_new = """
  <!-- HERO WITH VIDEO BACKGROUND -->
  <section class="about-hero" style="position: relative; min-height: 70vh; display: flex; align-items: center; background: #0b0f19; padding-top: var(--nav-height); overflow: hidden;">
    <!-- Video Background -->
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100vw; height: 100vw; min-height: 100vh; min-width: 177.77vh; z-index: 0; opacity: 0.4; pointer-events: none;">
      <iframe src="https://www.youtube.com/embed/xKxrkht7CpY?autoplay=1&mute=1&loop=1&playlist=xKxrkht7CpY&controls=0&disablekb=1&fs=0&modestbranding=1&playsinline=1" 
              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
              allow="autoplay; encrypted-media"></iframe>
    </div>
    
    <!-- High-tech Overlay -->
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(180deg, rgba(11,15,25,0.8) 0%, rgba(11,15,25,0.3) 50%, rgba(11,15,25,0.9) 100%); z-index: 1;"></div>
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: radial-gradient(rgba(0,255,255,0.1) 1px, transparent 1px); background-size: 30px 30px; z-index: 1;"></div>
    <div class="radar-scan" style="position: absolute; top: -100%; left: 0; right: 0; height: 20%; background: linear-gradient(to bottom, transparent, rgba(0,255,255,0.2), transparent); animation: scan 4s linear infinite; z-index: 1;"></div>

    <div class="container about-hero-content" style="position: relative; z-index: 2; max-width: 800px; padding: 60px 0 120px 0;">
      <h1 class="about-hero-title" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #fff; margin-bottom: 20px; text-transform: uppercase; text-shadow: 0 0 20px rgba(0,255,255,0.5);">SOLAR FORECASTING</h1>
      <p class="about-hero-subtitle" style="font-size: 1.2rem; color: #e2e8f0; margin-bottom: 30px; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">Powering a more stable, low-carbon solar power future</p>
      <a href="about.html#contact" class="btn btn-primary" style="background: rgba(0,0,0,0.5); border: 1px solid var(--accent-cyan); color: var(--accent-cyan); padding: 12px 24px; border-radius: 50px; text-decoration: none; font-weight: 500; transition: all 0.3s ease; backdrop-filter: blur(5px); box-shadow: 0 0 15px rgba(0,255,255,0.3);">Get in touch</a>
    </div>
  </section>
  
  <style>
    @keyframes scan {
      0% { top: -20%; }
      100% { top: 120%; }
    }
    .interactive-card {
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      position: relative;
      overflow: hidden;
    }
    .interactive-card:hover {
      transform: translateY(-10px) scale(1.02);
      box-shadow: 0 20px 40px rgba(0,255,255,0.15);
      border-color: var(--accent-cyan);
    }
    .interactive-card::after {
      content: '';
      position: absolute;
      top: -50%; left: -50%; width: 200%; height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
      opacity: 0;
      transition: opacity 0.3s;
      pointer-events: none;
    }
    .interactive-card:hover::after {
      opacity: 1;
      animation: rotate 10s linear infinite;
    }
    @keyframes rotate {
      100% { transform: rotate(360deg); }
    }
  </style>
"""

# Replace Hero
solar_html = re.sub(r'<!-- HERO -->.*?<!-- INTRO SECTION', solar_hero_new + '\n  <!-- INTRO SECTION', solar_html, flags=re.DOTALL)

# Add interactive images & videos for Solar Intro
solar_html = solar_html.replace(
    """<div style="width: 100%; height: 300px; background-image: url('assets/solutions/solar_panels_1.jpg'); background-size: cover; background-position: center; border-radius: 200px 200px 0 0; overflow: hidden; position: relative;">
          <!-- Placeholder or add image -->
        </div>""",
    """<div class="interactive-card" style="width: 100%; height: 350px; background-image: url('https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&q=80&w=1000'); background-size: cover; background-position: center; border-radius: 200px 200px 0 0; border: 2px solid #333; overflow: hidden; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
          <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 20px; background: linear-gradient(transparent, rgba(0,255,255,0.2)); text-align: center;">
            <span style="display: inline-block; padding: 5px 15px; border-radius: 20px; background: rgba(0,0,0,0.7); border: 1px solid var(--accent-cyan); color: var(--accent-cyan); font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; animation: pulse 2s infinite;">Live Satellite Feed</span>
          </div>
        </div>"""
)

solar_html = solar_html.replace(
    """<img src="assets/solutions/solar_panels_2.jpg" alt="Solar panels" style="width: 100%; border-radius: 8px;" onerror="this.src='https://via.placeholder.com/600x400/111/333?text=Solar+Panels'">""",
    """<div class="interactive-card" style="width: 100%; height: 300px; background-image: url('https://images.unsplash.com/photo-1584485532585-b1a7885b512c?auto=format&fit=crop&q=80&w=1000'); background-size: cover; background-position: center; border-radius: 12px; border: 1px solid #333; position: relative;">
         <div style="position: absolute; top: 20px; right: 20px; display: flex; gap: 10px;">
           <div style="width: 10px; height: 10px; border-radius: 50%; background: #00ff00; box-shadow: 0 0 10px #00ff00; animation: blink 1s infinite;"></div>
         </div>
         <div style="position: absolute; bottom: 20px; left: 20px; right: 20px; height: 60px; background: rgba(0,0,0,0.8); border-radius: 8px; border: 1px solid rgba(0,255,255,0.3); display: flex; align-items: center; padding: 0 20px; gap: 15px;">
           <div style="flex-grow: 1; height: 4px; background: #333; border-radius: 2px; position: relative; overflow: hidden;">
              <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 75%; background: var(--accent-cyan); animation: loadBar 3s infinite;"></div>
           </div>
           <span style="color: var(--accent-cyan); font-weight: bold; font-family: monospace;">AI SYNCHRONIZED</span>
         </div>
       </div>
       <style>
         @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
         @keyframes loadBar { 0% { width: 0%; } 50% { width: 95%; } 100% { width: 0%; } }
       </style>"""
)

# Update approach cards with interactive class
solar_html = solar_html.replace('style="background: var(--accent-cyan)', 'class="interactive-card" style="background: var(--accent-cyan)')


with open('solar-forecasting.html', 'w', encoding='utf-8') as f:
    f.write(solar_html)



# Update Wind Forecasting
with open('wind-forecasting.html', 'r', encoding='utf-8') as f:
    wind_html = f.read()

wind_hero_new = """
  <!-- HERO WITH VIDEO BACKGROUND -->
  <section class="about-hero" style="position: relative; min-height: 70vh; display: flex; align-items: center; background: #0b0f19; padding-top: var(--nav-height); overflow: hidden;">
    <!-- Video Background -->
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100vw; height: 100vw; min-height: 100vh; min-width: 177.77vh; z-index: 0; opacity: 0.4; pointer-events: none;">
      <iframe src="https://www.youtube.com/embed/NiYWN3r8h7g?autoplay=1&mute=1&loop=1&playlist=NiYWN3r8h7g&controls=0&disablekb=1&fs=0&modestbranding=1&playsinline=1" 
              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
              allow="autoplay; encrypted-media"></iframe>
    </div>
    
    <!-- High-tech Overlay -->
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(180deg, rgba(11,15,25,0.8) 0%, rgba(11,15,25,0.3) 50%, rgba(11,15,25,0.9) 100%); z-index: 1;"></div>
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: linear-gradient(0deg, transparent 24%, rgba(0, 255, 255, .05) 25%, rgba(0, 255, 255, .05) 26%, transparent 27%, transparent 74%, rgba(0, 255, 255, .05) 75%, rgba(0, 255, 255, .05) 76%, transparent 77%, transparent), linear-gradient(90deg, transparent 24%, rgba(0, 255, 255, .05) 25%, rgba(0, 255, 255, .05) 26%, transparent 27%, transparent 74%, rgba(0, 255, 255, .05) 75%, rgba(0, 255, 255, .05) 76%, transparent 77%, transparent); background-size: 50px 50px; z-index: 1;"></div>

    <div class="container about-hero-content" style="position: relative; z-index: 2; max-width: 800px; padding: 60px 0 120px 0;">
      <h1 class="about-hero-title" style="font-family: var(--font-display); font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 700; color: #fff; margin-bottom: 20px; text-transform: uppercase; text-shadow: 0 0 20px rgba(0,255,255,0.5);">WIND FORECASTING</h1>
      <p class="about-hero-subtitle" style="font-size: 1.2rem; color: #e2e8f0; margin-bottom: 30px; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">Precision forecasts for smarter wind operations</p>
      <a href="about.html#contact" class="btn btn-primary" style="background: rgba(0,0,0,0.5); border: 1px solid var(--accent-cyan); color: var(--accent-cyan); padding: 12px 24px; border-radius: 50px; text-decoration: none; font-weight: 500; transition: all 0.3s ease; backdrop-filter: blur(5px); box-shadow: 0 0 15px rgba(0,255,255,0.3);">Get in Touch</a>
    </div>
  </section>
"""

# Replace Hero
wind_html = re.sub(r'<!-- HERO -->.*?<!-- INTRO SECTION', wind_hero_new + '\n  <!-- INTRO SECTION', wind_html, flags=re.DOTALL)

# Add interactive images for Wind Intro
wind_html = wind_html.replace(
    """<img src="assets/solutions/wind_turbines.jpg" alt="Wind Turbines" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" onerror="this.src='https://via.placeholder.com/600x400/ddd/555?text=Wind+Turbines'">""",
    """<div class="interactive-card" style="width: 100%; height: 350px; background-image: url('https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&q=80&w=1000'); background-size: cover; background-position: center; border-radius: 12px; position: relative; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
         <!-- Interactive overlay -->
         <div style="position: absolute; inset: 0; background: linear-gradient(45deg, rgba(11,15,25,0.7) 0%, transparent 100%);"></div>
         <div style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.6); padding: 10px 15px; border-radius: 8px; border-left: 3px solid var(--accent-cyan); backdrop-filter: blur(4px);">
            <div style="color: var(--grey-300); font-size: 0.7rem; text-transform: uppercase; margin-bottom: 4px;">Live SCADA Feed</div>
            <div style="color: #fff; font-size: 1.2rem; font-weight: bold; font-family: monospace;">TBN-42: <span style="color: var(--accent-cyan);">OPTIMAL</span></div>
         </div>
         
         <svg style="position: absolute; bottom: 20px; right: 20px; width: 100px; height: 100px; animation: spin 4s linear infinite;" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" fill="none" stroke="rgba(0,255,255,0.3)" stroke-width="2" stroke-dasharray="10 5" />
            <circle cx="50" cy="50" r="35" fill="none" stroke="rgba(0,255,255,0.6)" stroke-width="1" />
            <path d="M50 15 L50 50 L85 50" fill="none" stroke="var(--accent-cyan)" stroke-width="3" />
         </svg>
       </div>
       <style>
         @keyframes spin { 100% { transform: rotate(360deg); } }
       </style>"""
)

# Update the dark cards
wind_html = wind_html.replace('style="background: var(--accent-cyan)', 'class="interactive-card" style="background: var(--accent-cyan)')

with open('wind-forecasting.html', 'w', encoding='utf-8') as f:
    f.write(wind_html)

print("Videos and interactive images added successfully.")
