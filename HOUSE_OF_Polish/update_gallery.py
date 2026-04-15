import re
import os

# Grab all valid images
valid_exts = {'.jpg', '.png', '.webp', '.jpeg'}
images = [f for f in os.listdir('.') if os.path.splitext(f.lower())[1] in valid_exts and f != 'about_us_2.heic' and f != '.DS_Store']
images.sort()

# Create HTML for gallery items
gallery_html_items = []
cats = ['manicure', 'pedicure', 'gel', 'art']

for i, img in enumerate(images):
    # Randomly assign categories for the filter to work beautifully
    cat = cats[i % len(cats)]
    item = f"""        <div class="gallery-item reveal" data-cat="{cat}" role="listitem" onclick="openLightbox(this)" data-label="Golden Nail Spa Collection">
          <img src="{img}" alt="Golden Nail Spa Collection" loading="lazy">
          <div class="gallery-item-overlay"><span class="gallery-item-label">Golden Nail Spa Collection</span></div>
        </div>"""
    gallery_html_items.append(item)

gallery_html = '<div class="gallery-grid" id="galleryGrid" role="list">\n' + '\n'.join(gallery_html_items) + '\n      </div>'

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to replace the old gallery grid
    pattern = re.compile(r'<div class="gallery-grid" id="galleryGrid" role="list">.*?</div>\n    </div>', re.DOTALL)
    content = pattern.sub(gallery_html + '\n    </div>', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Gallery completely updated with all images.")
