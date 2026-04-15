import re

css_target_old = r"""  /\* 4-column single row — each card fills one quarter \*/
  \.services-grid \{
    display: grid;
    grid-template-columns: repeat\(4, 1fr\);
    gap: 0 2\.5rem;
    max-width: 100%;
    margin: 0 auto;
  \}"""

css_target_new = """  /* 3-column layout for 6 items */
  .services-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 3.5rem 2.5rem;
    max-width: 100%;
    margin: 0 auto;
  }"""

files = ['/Users/thaophuong/Downloads/HOUSE_OF_Polish/index.html', '/Users/thaophuong/Downloads/HOUSE_OF_Polish/golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update CSS
    content = re.sub(css_target_old, css_target_new, content)
    
    # 2. Rebuild the services-grid HTML block
    is_house_of_polish = 'index.html' in file
    url_base = 'http://houseofpolishwv.com' if is_house_of_polish else 'http://goldennailandspa.com'
    
    html_new = f"""<div class="services-grid">

      <!-- Card 1 – Nail Services -->
      <div class="service-card reveal" role="button" tabindex="0"
           onclick="showPage('menu')" aria-label="Nail services">
        <div class="service-arch">
          <img src="{url_base}/wp-content/uploads/2026/04/IMG_5938-2.jpg"
               alt="Nail Services" loading="lazy">
        </div>
        <span class="service-card-name">Nail Services</span>
        <button class="service-card-btn" onclick="showPage('menu')" tabindex="-1">Show Services</button>
      </div>

      <!-- Card 2 – Manicures -->
      <div class="service-card reveal reveal-delay-1" role="button" tabindex="0"
           onclick="showPage('menu')" aria-label="Manicure services">
        <div class="service-arch">
          <img src="{url_base}/wp-content/uploads/2026/04/healthy-beautiful-manicure-manicurist-scaled.jpg"
               alt="Manicures" loading="lazy">
        </div>
        <span class="service-card-name">Manicures</span>
        <button class="service-card-btn" onclick="showPage('menu')" tabindex="-1">Show Services</button>
      </div>

      <!-- Card 3 – Pedicures -->
      <div class="service-card reveal reveal-delay-2" role="button" tabindex="0"
           onclick="showPage('menu')" aria-label="Pedicure services">
        <div class="service-arch">
          <img src="{url_base}/wp-content/uploads/2026/04/1_1559892132_6_pedicure_slide3.jpg"
               alt="Pedicures" loading="lazy">
        </div>
        <span class="service-card-name">Pedicures</span>
        <button class="service-card-btn" onclick="showPage('menu')" tabindex="-1">Show Services</button>
      </div>

      <!-- Card 4 – Kid Services -->
      <div class="service-card reveal" role="button" tabindex="0"
           onclick="showPage('menu')" aria-label="Kid services">
        <div class="service-arch">
          <img src="{url_base}/wp-content/uploads/2026/04/71b4B6adKPL.jpg"
               alt="Kid Services" loading="lazy">
        </div>
        <span class="service-card-name">Kid Services</span>
        <button class="service-card-btn" onclick="showPage('menu')" tabindex="-1">Show Services</button>
      </div>

      <!-- Card 5 – Waxing -->
      <div class="service-card reveal reveal-delay-1" role="button" tabindex="0"
           onclick="showPage('menu')" aria-label="Waxing services">
        <div class="service-arch">
          <img src="{url_base}/wp-content/uploads/2026/04/woman-getting-her-leg-hair-removed-scaled.jpg"
               alt="Waxing" loading="lazy" style="object-position:center 15%;">
        </div>
        <span class="service-card-name">Waxing</span>
        <button class="service-card-btn" onclick="showPage('menu')" tabindex="-1">Show Services</button>
      </div>

      <!-- Card 6 – Eyelash Extensions -->
      <div class="service-card reveal reveal-delay-2" role="button" tabindex="0"
           onclick="showPage('menu')" aria-label="Eyelash extensions">
        <div class="service-arch">
          <img src="{url_base}/wp-content/uploads/2026/04/classic-lash-extensions_40f6766c-6dca-48bd-874d-baa52383830b.jpg"
               alt="Eyelash Extensions" loading="lazy" style="object-position:center 20%;">
        </div>
        <span class="service-card-name">Eyelash Extensions</span>
        <button class="service-card-btn" onclick="showPage('menu')" tabindex="-1">Show Services</button>
      </div>

    </div><!-- /.services-grid -->"""
    
    # find everything between <div class="services-grid"> and </div><!-- /.services-grid -->
    pattern = re.compile(r'<div class="services-grid">.*?</div><!-- /.services-grid -->', re.DOTALL)
    content = pattern.sub(html_new, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates applied.")
