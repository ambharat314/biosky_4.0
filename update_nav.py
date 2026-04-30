import os
import glob

# CSS to append
dropdown_css = """
/* ===== NAV DROPDOWN ===== */
.nav-dropdown {
  position: relative;
  display: inline-block;
}

.nav-dropdown-content {
  display: none;
  position: absolute;
  background-color: rgba(11, 15, 25, 0.95);
  min-width: 200px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.5);
  z-index: 100;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 0;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.nav-dropdown-content a {
  color: var(--grey-300);
  padding: 12px 20px;
  text-decoration: none;
  display: block;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}

.nav-dropdown-content a:hover {
  background-color: rgba(255, 255, 255, 0.05);
  color: var(--accent-cyan);
}

.nav-dropdown:hover .nav-dropdown-content {
  display: block;
  animation: fadeIn 0.2s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translate(-50%, 10px); }
  to { opacity: 1; transform: translate(-50%, 0); }
}

@media (max-width: 768px) {
  .nav-dropdown-content {
    position: static;
    display: none;
    box-shadow: none;
    background: transparent;
    border: none;
    transform: none;
    padding-left: 20px;
  }
  .nav-dropdown:hover .nav-dropdown-content {
    display: block;
  }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(dropdown_css)

html_files = glob.glob('*.html')

old_nav_link = '<a href="solutions.html" class="nav-link">Solutions</a>'
new_nav_dropdown = """<div class="nav-dropdown">
        <a href="solutions.html" class="nav-link">Solutions <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-left: 2px;"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="nav-dropdown-content">
          <a href="solar-forecasting.html">Solar Forecasting</a>
          <a href="wind-forecasting.html">Wind Forecasting</a>
        </div>
      </div>"""

# Ensure the spacing matches for replace (the exact string in index.html is '<a href="solutions.html" class="nav-link">Solutions</a>')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_nav_link in content:
        content = content.replace(old_nav_link, new_nav_dropdown)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated {file}")
    elif new_nav_dropdown in content:
        print(f"Already updated {file}")
    else:
        # Try a regex in case of slight whitespace differences
        import re
        pattern = r'<a\s+href="solutions\.html"\s+class="nav-link"\s*>\s*Solutions\s*</a>'
        if re.search(pattern, content):
            content = re.sub(pattern, new_nav_dropdown, content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Updated {file} (regex)")
        else:
            print(f"Could not find solutions link in {file}")

print("Navigation update complete.")
