import re

menu_html = """<div class="menu-grid">
        <!-- Nail Services -->
        <div class="menu-category reveal">
          <div class="menu-cat-title"><em>Nail Services</em></div>
          <div class="menu-cat-sub">Enhancements & Dipping</div>
          
          <div class="menu-item" style="margin-bottom:0.5rem;font-size:0.85rem;display:flex;justify-content:flex-end;gap:1.5rem;opacity:0.7;text-transform:uppercase;"><span>Full Set</span><span>Fill-in</span></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Ombre/ Pink &amp; White</span><span class="menu-item-dots"></span><span class="menu-item-price">$55 / $50</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Shellac</span><span class="menu-item-dots"></span><span class="menu-item-price">$50 / $45</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Overlay</span><span class="menu-item-dots"></span><span class="menu-item-price">$45 / $40</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">American Tip/ White Tip</span><span class="menu-item-dots"></span><span class="menu-item-price">$50 / $45</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Tap Gel</span><span class="menu-item-dots"></span><span class="menu-item-price">$55 / $50</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Gel-X</span><span class="menu-item-dots"></span><span class="menu-item-price">$55 / $50</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Builder Gel</span><span class="menu-item-dots"></span><span class="menu-item-price">$55 / $50</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Dipping</span><span class="menu-item-dots"></span><span class="menu-item-price">$45</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Dipping &amp; Basic Manicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$60</span></div></div>
        </div>

        <!-- Manicures -->
        <div class="menu-category reveal reveal-delay-1">
          <div class="menu-cat-title"><em>Manicures</em></div>
          <div class="menu-cat-sub">Hand Care</div>
          
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">1. Classic Manicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$25</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Enjoy nail shaping, cuticle treatment, and massage with lotion. Finished with regular polish for a clean look.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">2. Shellac Manicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$35</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Includes shaping, cuticle treatment, soothing massage, and your choice of flawless, chip-resistant gel polish.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">3. Golden Manicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$50</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Includes all basics plus sugar scrub, collagen wrap, and 10-minute massage with hot stones and hot towels.</div>
          </div>
          
          <!-- Complimentary Drinks Section (Placed centrally) -->
          <div class="menu-item" style="margin-top: 1.5rem; text-align:center;">
             <em style="color:#D4AF37;">Complimentary Beverages</em><br>
             <span style="font-size:0.85rem;opacity:0.8;">Enjoy Bottled Water, Soft Drinks, Wine, or House Margaritas.</span><br><br>
             <em style="color:#D4AF37;">Signature Spa Drinks</em><br>
             <span style="font-size:0.85rem;opacity:0.8;">Complimentary with any $55+ Mani or Pedi. Pick from: Pink Rose Soda, Golden Lychee Cloud, Blue Velvet Berry, Sunset Orange Glow. Sip • Relax • Indulge</span>
          </div>
        </div>

        <!-- Pedicures -->
        <div class="menu-category reveal">
          <div class="menu-cat-title"><em>Pedicures</em></div>
          <div class="menu-cat-sub">Ultimate Foot Retreat</div>
          
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">1. Golden Ultimate Pedicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$99</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Steam eye mask, herbal gloves, Gold Detox Bomb, 24K gold flakes and collagen hydration mask. 30-minute full massage with hot stones and warm candle oil.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">2. Herbal Detox Spa (Best Seller)</span><span class="menu-item-dots"></span><span class="menu-item-price">$85</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Detoxifies and cleanses. Includes shoulder/neck wrap, steam eye mask, paraffin dry heel treatment. 25-minute massage with hot stones.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">3. Luxury Jelly Pedicure (Best Seller)</span><span class="menu-item-dots"></span><span class="menu-item-price">$85</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Soothes aching joints with Jelly spa heat therapy. Includes wrap, eye mask, paraffin wax, and 25-minute massage.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">4. Signature Therapy (Best Seller)</span><span class="menu-item-dots"></span><span class="menu-item-price">$79</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Mineral pedi bomb, sugar scrub, paraffin wax, and 20-minute hot stone massage. (7 Scent Options)</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">5. Volcano Crystal Pedicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$70</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Volcano eruption soak experience. Paraffin wax and 18-minute hot stone massage.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">6. Tropical Pedicure (Best Seller)</span><span class="menu-item-dots"></span><span class="menu-item-price">$60</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Tropical soak and 12-minute massage with warm candle oil. (5 Scent Options)</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">7. Organic Fiji Coconut</span><span class="menu-item-dots"></span><span class="menu-item-price">$50</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Coconut sugar scrub and 10-minute massage with exotic coconut lotion.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">8. Deluxe Pedicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$40</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Deep hydration mask with an 8-minute foot massage and hot towels.</div>
          </div>
          <div class="menu-item">
            <div class="menu-item-main"><span class="menu-item-name">9. Classic Pedicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$35</span></div>
            <div class="menu-subitem" style="opacity: 0.8; font-size: 0.85rem; line-height: 1.4; display:block; text-align:left;">Gentle trimming, sugar scrub, callus removal, and 5-minute massage.</div>
          </div>
          <br>
          <div class="menu-cat-title" style="font-size:1.2rem;"><em>Pedicure Extras</em></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Gel/Shellac Add-on</span><span class="menu-item-dots"></span><span class="menu-item-price">$15</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Extra Massage (10 Mins)</span><span class="menu-item-dots"></span><span class="menu-item-price">$15</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Acrylic on Toes - Full Set</span><span class="menu-item-dots"></span><span class="menu-item-price">$50</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Acrylic on Toes - Refill</span><span class="menu-item-dots"></span><span class="menu-item-price">$45</span></div></div>
          <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Acrylic on Toes - 1 Big Toe</span><span class="menu-item-dots"></span><span class="menu-item-price">$5</span></div></div>
        </div>

        <div style="display:flex; flex-direction:column; gap:2rem;">
          <!-- Kids Services -->
          <div class="menu-category reveal reveal-delay-1">
            <div class="menu-cat-title"><em>Kids' Services</em></div>
            <div class="menu-cat-sub">Under 12 years old &amp; under 5 ft</div>
            
            <div class="menu-item">
              <div class="menu-item-main"><span class="menu-item-name">Kids' Manicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$20</span></div>
            </div>
            <div class="menu-item">
              <div class="menu-item-main"><span class="menu-item-name">Kids' Pedicure</span><span class="menu-item-dots"></span><span class="menu-item-price">$30</span></div>
            </div>
          </div>

          <!-- Add-ons -->
          <div class="menu-category reveal reveal-delay-1">
            <div class="menu-cat-title"><em>Additional Services</em></div>
            <div class="menu-cat-sub">Enhance Your Vibe</div>
            
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Nail Take-Off</span><span class="menu-item-dots"></span><span class="menu-item-price">$15</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Nail/Toe Trim</span><span class="menu-item-dots"></span><span class="menu-item-price">$10</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Hand Polish Change</span><span class="menu-item-dots"></span><span class="menu-item-price">$10</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Toe Polish Change</span><span class="menu-item-dots"></span><span class="menu-item-price">$10</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Shellac Change</span><span class="menu-item-dots"></span><span class="menu-item-price">$20</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Paraffin Wax</span><span class="menu-item-dots"></span><span class="menu-item-price">$8</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Hot Stone</span><span class="menu-item-dots"></span><span class="menu-item-price">$5</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Collagen Mask</span><span class="menu-item-dots"></span><span class="menu-item-price">$10</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Shape / Length / French / Design</span><span class="menu-item-dots"></span><span class="menu-item-price">$5+ (ea)</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Chrome / Cat Eye</span><span class="menu-item-dots"></span><span class="menu-item-price">$10 (ea)</span></div></div>
          </div>
          
          <!-- Eyelash Extensions -->
          <div class="menu-category reveal reveal-delay-1">
            <div class="menu-cat-title"><em>Eyelashes</em></div>
            <div class="menu-cat-sub">Volume &amp; Definition</div>
            
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Volume Lash</span><span class="menu-item-dots"></span><span class="menu-item-price">$160</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Wispy Lash</span><span class="menu-item-dots"></span><span class="menu-item-price">$150</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Hybrid Lash</span><span class="menu-item-dots"></span><span class="menu-item-price">$140</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">3D Classic Lash</span><span class="menu-item-dots"></span><span class="menu-item-price">$120</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Classic Lash</span><span class="menu-item-dots"></span><span class="menu-item-price">$90</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Lash Fill-In</span><span class="menu-item-dots"></span><span class="menu-item-price">$65+</span></div></div>
          </div>

          <!-- Waxing -->
          <div class="menu-category reveal reveal-delay-1">
            <div class="menu-cat-title"><em>Waxing</em></div>
            
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Eyebrows / Chin / Nose / Ears</span><span class="menu-item-dots"></span><span class="menu-item-price">$10 (ea)</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Lips</span><span class="menu-item-dots"></span><span class="menu-item-price">$7</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Sideburns</span><span class="menu-item-dots"></span><span class="menu-item-price">$12</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Whole Face</span><span class="menu-item-dots"></span><span class="menu-item-price">$40</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Underarms</span><span class="menu-item-dots"></span><span class="menu-item-price">$25</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Half / Full Arms</span><span class="menu-item-dots"></span><span class="menu-item-price">$25 / $40</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Half / Full Legs</span><span class="menu-item-dots"></span><span class="menu-item-price">$35 / $65</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Chest</span><span class="menu-item-dots"></span><span class="menu-item-price">$35+</span></div></div>
            <div class="menu-item"><div class="menu-item-main"><span class="menu-item-name">Back</span><span class="menu-item-dots"></span><span class="menu-item-price">$70+</span></div></div>
          </div>

        </div>
      </div>"""

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the old menu-grid
    pattern = re.compile(r'<div class="menu-grid">.*?</div>\n    </div>\n\n    <!-- ════════════', re.DOTALL)
    content = pattern.sub(menu_html + '\n    </div>\n\n    <!-- ════════════', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Menu fully updated from document.")
