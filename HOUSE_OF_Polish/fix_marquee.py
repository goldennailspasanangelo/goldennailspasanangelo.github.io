import re

files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all leftover product-img-wrap divs that refer to external URLs or the old IMG_2026... URLs
    # Since we replaced the inside of the marquee with the new images, the garbage left over are precisely
    # the ones containing `IMG_59` or `IMG_2026` or `White-Modern`.
    
    # Wait, the best way is to remove any `<div class="product-img-wrap">...</div>` that appears AFTER `</div>\n  </section>\n\n  <footer`...
    # Oh wait, the `</section>` might have been deleted by the previous bad regex!
    
    # Let's see if `</section>` is there.
    # In the view_file, line 2074 is `    </div>`. Line 2075 is `<div class="product-...>`.
    # It seems the `</section>` was overwritten!
    
    # We must properly restore the end of products-section and then the footer.
    
    pattern = re.compile(
        r'(<div class="products-marquee reveal reveal-delay-2">.*?</div>\n    </div>)\n\s*<div class="product-img-wrap">.*?(<footer role="contentinfo">)',
        re.DOTALL
    )
    
    content = pattern.sub(r'\1\n  </section>\n\n  \2', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed leftover elements.")
