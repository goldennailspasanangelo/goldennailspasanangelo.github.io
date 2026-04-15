import re

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Menu Fonts
    content = re.sub(
        r'\.menu-cat-title \{\s*font-family: \'Cormorant Garamond\', serif;\s*font-weight: 300;\s*font-size: 1\.6rem;',
        r'.menu-cat-title {\n    font-family: \'Cormorant Garamond\', serif;\n    font-weight: 400;\n    font-size: 2.2rem;',
        content
    )
    content = re.sub(
        r'\.menu-cat-sub \{\s*font-size: 0\.65rem;',
        r'.menu-cat-sub {\n    font-size: 0.85rem;\n    font-weight: 500;',
        content
    )
    content = re.sub(
        r'\.menu-item-name \{\s*font-size: 0\.85rem;',
        r'.menu-item-name {\n    font-size: 1.15rem;',
        content
    )
    content = re.sub(
        r'\.menu-item-price \{\s*font-size: 0\.85rem;',
        r'.menu-item-price {\n    font-size: 1.15rem;',
        content
    )
    content = re.sub(
        r'font-size: 0\.78rem;\s*color: rgba\(28,20,0,0\.45\);',
        r'font-size: 0.95rem;\n    color: rgba(28,20,0,0.6);',
        content
    )
    
    # Let's fix the inline sizes from when we built the menu:
    content = re.sub(r'font-size:0\.85rem;', 'font-size:1rem;', content)

    # 2. Add Mobile FAB (Floating Action Button) just before </body>
    fab_html = """
<a href="https://pronailsii6073.simplepos.us/" target="_blank" class="mobile-fab" aria-label="Book Online">Book Online</a>
<style>
  .mobile-fab {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    background: var(--gold-light);
    color: #fff;
    padding: 1rem 1.8rem;
    border-radius: 30px;
    font-family: 'Jost', sans-serif;
    letter-spacing: 0.1em;
    font-weight: 500;
    font-size: 0.9rem;
    text-transform: uppercase;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(212,175,55,0.4);
    animation: bounce 2s infinite;
  }
  @media (max-width: 768px) {
    .mobile-fab { display: block; }
  }
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
    40% {transform: translateY(-8px);}
    60% {transform: translateY(-4px);}
  }
</style>
</body>"""
    content = re.sub(r'</body>', fab_html, content)

    # 3. Replace all "Book Appointment" buttons mapped to contact to instead go to simplepos
    btn_old = r'<span class="btn btn-primary" onclick="showPage\(\'contact\'\)" role="link" tabindex="0">Book Appointment</span>'
    btn_new = r'<a href="https://pronailsii6073.simplepos.us/" target="_blank" class="btn btn-primary" style="text-decoration:none;">Book Online</a>'
    content = re.sub(btn_old, btn_new, content)

    # 4. Insert Menu Banner Image
    old_menu_banner = r'<div class="page-section" id="page-menu">\s*<div class="inner-page">\s*<div class="page-hero" role="banner">'
    new_menu_banner = r"""<div class="page-section" id="page-menu">
  <div class="inner-page">
    <div class="page-hero" role="banner" style="background-image: url('banner_1.webp'); background-size: cover; background-position: center; position: relative;">
      <!-- Overlay to ensure text readability -->
      <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.4);"></div>
      <div style="position: relative; z-index: 2;">"""
    
    # I also need to close the extra div I added:
    content = re.sub(old_menu_banner, new_menu_banner, content)
    
    # We replaced `<div class="page-hero" role="banner">` which enclosed:
    # <div>
    #   <div class="page-hero-sub">Services &amp; Pricing</div>
    #   <h1 class="page-hero-title">Our <em>Menu</em></h1>
    # </div>
    # So we need to close the `div style="position: relative; z-index: 2;"`
    # Let's fix that specifically for the menu:
    old_menu_hero_close = r'<h1 class="page-hero-title">Our <em>Menu</em></h1>\s*</div>\s*</div>'
    new_menu_hero_close = r'<h1 class="page-hero-title">Our <em>Menu</em></h1>\n      </div>\n      </div>\n    </div>'
    content = re.sub(old_menu_hero_close, new_menu_hero_close, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied font resizing, Book Online links, mobile FAB, and Menu banner!")
