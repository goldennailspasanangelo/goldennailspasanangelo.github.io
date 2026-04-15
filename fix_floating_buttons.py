import re

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the broken backslash quotes in the Service Card buttons
    # We must replace `showPage(\'menu\', \'menu-nails\')` with `showPage('menu', 'menu-nails')`
    content = content.replace(r"\'", "'")
    
    # 2. Add floating 'Call Now' and 'Book Now' buttons visually.
    # I previously injected a `.mobile-fab` right before `</body>`.
    # Let's completely remove `.mobile-fab` first.
    clean_content = re.sub(r'<a href="https://pronailsii6073\.simplepos\.us/" target="_blank" class="mobile-fab"[^>]*>Book Online</a>', '', content)
    clean_content = re.sub(r'<style>\s*\.mobile-fab \{.*?\}</style>', '', clean_content, flags=re.DOTALL)
    
    # Create the beautiful dual-button floating container
    dual_fab_html = """
<div class="floating-actions" role="group" aria-label="Quick Actions">
  <a href="tel:+13259470470" class="fab-btn fab-call" aria-label="Call Now">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
    Call Now
  </a>
  <a href="https://pronailsii6073.simplepos.us/" target="_blank" class="fab-btn fab-book" aria-label="Book Online">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
    Book Now
  </a>
</div>
<style>
  .floating-actions {
    position: fixed;
    bottom: 25px;
    right: 25px;
    display: flex;
    gap: 12px;
    z-index: 9999;
    animation: fadeUpIn 1s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
  }
  .fab-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 0.95rem 1.6rem;
    border-radius: 30px;
    font-family: 'Jost', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    text-decoration: none;
    box-shadow: 0 8px 25px rgba(28,20,0,0.15);
    transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.3s;
  }
  .fab-btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 35px rgba(28,20,0,0.25);
  }
  .fab-call {
    background: #FFF;
    color: #1C1400;
    border: 1px solid rgba(212,175,55,0.4);
  }
  .fab-book {
    background: var(--gold-light);
    color: #FFF;
  }
  @keyframes fadeUpIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  @media (max-width: 768px) {
    .floating-actions {
      bottom: 15px;
      left: 15px;
      right: 15px;
      justify-content: space-between;
      gap: 10px;
    }
    .fab-btn {
      flex: 1;
      justify-content: center;
      padding: 0.85rem 1rem;
      font-size: 0.85rem;
    }
  }
</style>
</body>"""
    # Just in case `</body>` was replaced, ensure we replace `</body>`
    clean_content = clean_content.replace('</body>', dual_fab_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(clean_content)

print("Bugs fixed! Floating dual-action buttons injected and syntax quotes corrected!")
