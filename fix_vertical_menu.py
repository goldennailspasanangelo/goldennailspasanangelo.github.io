import re

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS .menu-grid
    css_old = r""".menu-grid \{
    display: grid;
    grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\);
    gap: 2px;
    margin-top: 3rem;
  \}"""
    css_new = """.menu-grid {
    display: flex;
    flex-direction: column;
    max-width: 800px;
    margin: 3rem auto 0;
    gap: 2rem;
  }"""
    content = re.sub(css_old, css_new, content)
    
    # 2. Add anchors to Menu Categories
    cat_nails = r'<div class="menu-category reveal">\s*<div class="menu-cat-title"><em>Nail Services'
    cat_nails_new = r'<div class="menu-category reveal" id="menu-nails">\n          <div class="menu-cat-title"><em>Nail Services'
    content = re.sub(cat_nails, cat_nails_new, content)

    cat_mani = r'<div class="menu-category reveal reveal-delay-1">\s*<div class="menu-cat-title"><em>Manicures'
    cat_mani_new = r'<div class="menu-category reveal reveal-delay-1" id="menu-manicures">\n          <div class="menu-cat-title"><em>Manicures'
    content = re.sub(cat_mani, cat_mani_new, content)

    cat_pedi = r'<div class="menu-category reveal">\s*<div class="menu-cat-title"><em>Pedicures'
    cat_pedi_new = r'<div class="menu-category reveal" id="menu-pedicures">\n          <div class="menu-cat-title"><em>Pedicures'
    content = re.sub(cat_pedi, cat_pedi_new, content)

    cat_kids = r'<div class="menu-category reveal reveal-delay-1">\s*<div class="menu-cat-title"><em>Kids\' Services'
    cat_kids_new = r'<div class="menu-category reveal reveal-delay-1" id="menu-kids">\n            <div class="menu-cat-title"><em>Kids\' Services'
    content = re.sub(cat_kids, cat_kids_new, content)

    cat_waxing = r'<div class="menu-category reveal reveal-delay-1">\s*<div class="menu-cat-title"><em>Waxing'
    cat_waxing_new = r'<div class="menu-category reveal reveal-delay-1" id="menu-waxing">\n            <div class="menu-cat-title"><em>Waxing'
    content = re.sub(cat_waxing, cat_waxing_new, content)
    
    cat_lashes = r'<div class="menu-category reveal reveal-delay-1">\s*<div class="menu-cat-title"><em>Eyelashes'
    cat_lashes_new = r'<div class="menu-category reveal reveal-delay-1" id="menu-eyelashes">\n            <div class="menu-cat-title"><em>Eyelashes'
    content = re.sub(cat_lashes, cat_lashes_new, content)

    # 3. Update Home Page Service Cards to point to Anchors
    serv_nails = r'<span class="service-card-name">Nail Services</span>\s*<button class="service-card-btn" onclick="showPage\(\'menu\'\)"'
    serv_nails_new = r'<span class="service-card-name">Nail Services</span>\n        <button class="service-card-btn" onclick="showPage(\'menu\', \'menu-nails\')"'
    content = re.sub(serv_nails, serv_nails_new, content)

    serv_mani = r'<span class="service-card-name">Manicures</span>\s*<button class="service-card-btn" onclick="showPage\(\'menu\'\)"'
    serv_mani_new = r'<span class="service-card-name">Manicures</span>\n        <button class="service-card-btn" onclick="showPage(\'menu\', \'menu-manicures\')"'
    content = re.sub(serv_mani, serv_mani_new, content)

    serv_pedi = r'<span class="service-card-name">Pedicures</span>\s*<button class="service-card-btn" onclick="showPage\(\'menu\'\)"'
    serv_pedi_new = r'<span class="service-card-name">Pedicures</span>\n        <button class="service-card-btn" onclick="showPage(\'menu\', \'menu-pedicures\')"'
    content = re.sub(serv_pedi, serv_pedi_new, content)

    serv_kids = r'<span class="service-card-name">Kid Services</span>\s*<button class="service-card-btn" onclick="showPage\(\'menu\'\)"'
    serv_kids_new = r'<span class="service-card-name">Kid Services</span>\n        <button class="service-card-btn" onclick="showPage(\'menu\', \'menu-kids\')"'
    content = re.sub(serv_kids, serv_kids_new, content)

    serv_waxing = r'<span class="service-card-name">Waxing</span>\s*<button class="service-card-btn" onclick="showPage\(\'menu\'\)"'
    serv_waxing_new = r'<span class="service-card-name">Waxing</span>\n        <button class="service-card-btn" onclick="showPage(\'menu\', \'menu-waxing\')"'
    content = re.sub(serv_waxing, serv_waxing_new, content)

    serv_lashes = r'<span class="service-card-name">Eyelash Extensions</span>\s*<button class="service-card-btn" onclick="showPage\(\'menu\'\)"'
    serv_lashes_new = r'<span class="service-card-name">Eyelash Extensions</span>\n        <button class="service-card-btn" onclick="showPage(\'menu\', \'menu-eyelashes\')"'
    content = re.sub(serv_lashes, serv_lashes_new, content)

    # 4. Update showPage function to accept anchor and scroll
    # From: function showPage(page) {
    # To:   function showPage(page, anchorId=null) {
    showpage_old = r'function showPage\(page\) \{'
    showpage_new = r'function showPage(page, anchorId=null) {'
    content = re.sub(showpage_old, showpage_new, content)

    scroll_old = r'window\.scrollTo\(\{ top: 0, behavior: \'smooth\' \}\);'
    scroll_new = r"""if (anchorId) {
      setTimeout(function() {
        var el = document.getElementById(anchorId);
        if (el) {
          var y = el.getBoundingClientRect().top + window.pageYOffset - 100; // Offset for fixed nav
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }, 50);
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }"""
    content = re.sub(scroll_old, scroll_new, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Menu Vertical layout and Smart linking applied!")
