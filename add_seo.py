import os
import glob
from bs4 import BeautifulSoup

html_files = glob.glob('*.html')

seo_data = {
    'index.html': {
        'title': 'BioSky — Space-Powered Energy Intelligence',
        'desc': 'BioSky Space Innovations builds a unified intelligence layer combining satellite data, AI models, and grid analytics for renewable energy forecasting, grid intelligence, and climate resilience.',
        'url': 'https://biosky.tech/'
    },
    'about.html': {
        'title': 'BioSky — About Us | Space-Powered Energy Intelligence',
        'desc': 'Learn about BioSky Space Innovations. We are a spacetech company using AI and Satellite Imagery to power India\'s energy resilience.',
        'url': 'https://biosky.tech/about.html'
    },
    'platform.html': {
        'title': 'BioSky Platform — AI & Satellite Energy Intelligence Stack',
        'desc': 'Explore BioSky\'s core platform: DeepSky Vision, GridMind AI, and ClimateCast. We merge multi-spectral satellite imagery with advanced ML to deliver actionable grid intelligence.',
        'url': 'https://biosky.tech/platform.html'
    },
    'solutions.html': {
        'title': 'BioSky Solutions — Solar, Wind & Grid Forecasting',
        'desc': 'Discover BioSky\'s solutions for grid operators, energy traders, and renewable developers. We provide high-accuracy solar forecasting, wind forecasting, and anomaly detection.',
        'url': 'https://biosky.tech/solutions.html'
    },
    'solar-forecasting.html': {
        'title': 'Solar Forecasting — BioSky Space Innovations',
        'desc': 'High-accuracy, intra-day, and day-ahead solar generation forecasting using cloud-tracking satellite imagery, irradiance modeling, and localized AI weather models.',
        'url': 'https://biosky.tech/solar-forecasting.html'
    },
    'wind-forecasting.html': {
        'title': 'Wind Forecasting — BioSky Space Innovations',
        'desc': 'Advanced wind power generation forecasting. BioSky uses high-resolution atmospheric modeling, satellite terrain mapping, and turbine-level wake effect AI.',
        'url': 'https://biosky.tech/wind-forecasting.html'
    },
    'careers.html': {
        'title': 'Careers at BioSky — Join the Spacetech Revolution',
        'desc': 'Join the team at BioSky Space Innovations. We are looking for passionate data scientists, spacetech engineers, and climate analysts to build the future of energy.',
        'url': 'https://biosky.tech/careers.html'
    }
}

for file_path in html_files:
    if file_path not in seo_data:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    head = soup.head
    if not head:
        continue
        
    data = seo_data[file_path]
    
    # Update title
    if soup.title:
        soup.title.string = data['title']
    else:
        new_title = soup.new_tag('title')
        new_title.string = data['title']
        head.append(new_title)
        
    # Remove existing meta descriptions, og: tags, twitter tags, canonical to avoid duplicates
    tags_to_remove = []
    for tag in head.find_all('meta'):
        if not tag.attrs:
            continue
        name = tag.attrs.get('name', '')
        prop = tag.attrs.get('property', '')
        if isinstance(name, list): name = name[0]
        if isinstance(prop, list): prop = prop[0]
            
        if name in ['description', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']:
            tags_to_remove.append(tag)
        elif prop.startswith('og:'):
            tags_to_remove.append(tag)
            
    for tag in head.find_all('link', rel='canonical'):
        tags_to_remove.append(tag)
        
    for tag in tags_to_remove:
        tag.decompose()
        
    # Helper to add meta tag
    def add_meta(name_attr, name_val, content):
        tag = soup.new_tag('meta')
        tag[name_attr] = name_val
        tag['content'] = content
        head.append(tag)
        
    # Add new SEO tags
    add_meta('name', 'description', data['desc'])
    
    # Open Graph
    add_meta('property', 'og:type', 'website')
    add_meta('property', 'og:url', data['url'])
    add_meta('property', 'og:title', data['title'])
    add_meta('property', 'og:description', data['desc'])
    add_meta('property', 'og:image', 'https://biosky.tech/assets/satellite.jpg')
    
    # Twitter
    add_meta('name', 'twitter:card', 'summary_large_image')
    add_meta('name', 'twitter:url', data['url'])
    add_meta('name', 'twitter:title', data['title'])
    add_meta('name', 'twitter:description', data['desc'])
    add_meta('name', 'twitter:image', 'https://biosky.tech/assets/satellite.jpg')
    
    # Canonical
    canonical = soup.new_tag('link')
    canonical['rel'] = 'canonical'
    canonical['href'] = data['url']
    head.append(canonical)
    
    # Write back
    # Use formatter to prevent modifying HTML entity encodings excessively if not needed, but BS4 defaults are usually fine
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated SEO for {file_path}")

