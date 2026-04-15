import re
import os

images = [f for f in os.listdir('.') if re.match(r'\d+_\d+_\d+_n\.jpg', f)]
images.sort()

# Create HTML for main slider
main_slider_html = '\n'.join([f'        <div class="product-img-wrap"><img src="{img}" loading="lazy" alt="Product item"><div class="product-overlay"><span class="product-btn" onclick="showPage(\'contact\')" role="link" tabindex="0">Shop Now</span></div></div>' for img in images])

# Create HTML for cloned slider
cloned_slider_html = '\n'.join([f'        <div class="product-img-wrap"><img src="{img}" loading="lazy" alt="Product item"><div class="product-overlay"><span class="product-btn" onclick="showPage(\'contact\')" role="link" tabindex="-1">Shop Now</span></div></div>' for img in images])

new_marquee_html = f"""<div class="products-marquee reveal reveal-delay-2">
      <!-- Original Slider -->
      <div class="products-slider">
{main_slider_html}
      </div>
      
      <!-- Cloned Slider to make scroll infinite seamlessly -->
      <div class="products-slider" aria-hidden="true">
{cloned_slider_html}
      </div>
    </div>"""

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to replace the old marquee
    pattern = re.compile(r'<div class="products-marquee[^>]*>.*?</div>\s*</div>', re.DOTALL)
    content = pattern.sub(new_marquee_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Marquee updated.")
