import re

files = ['/Users/thaophuong/Downloads/HOUSE_OF_Polish/index.html', '/Users/thaophuong/Downloads/HOUSE_OF_Polish/golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The old block
    old_block_pattern = re.compile(
        r'<div class="about-collage reveal">.*?<div class="collage-item">.*?<img src="[^"]*IMG_5942\.jpg".*?</div>\n      </div>',
        re.DOTALL
    )

    new_block = """<div class="about-collage reveal">
        <div class="about-img-accent" aria-hidden="true" style="width:70%; height:80%; bottom:-20px; left:-20px;"></div>
        <div class="collage-item" style="aspect-ratio: 3/4; transform: translateY(2rem); box-shadow: 0 10px 30px rgba(0,0,0,0.15); border-radius: 4px;">
          <img src="about_us_1.JPG" alt="About Us" loading="lazy">
        </div>
        <div class="collage-item" style="aspect-ratio: 3/4; box-shadow: 0 10px 30px rgba(0,0,0,0.15); border-radius: 4px;">
          <img src="about_us_2.heic" alt="About Us" loading="lazy">
        </div>
      </div>"""

    content = old_block_pattern.sub(new_block, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("About Us elegant images applied.")
