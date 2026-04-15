import os

files = ['/Users/thaophuong/Downloads/HOUSE_OF_Polish/index.html', '/Users/thaophuong/Downloads/HOUSE_OF_Polish/golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Phone numbers
    content = content.replace('(304) 845-2727', '(325) 947-0470')
    content = content.replace('+13048452727', '+13259470470')
    content = content.replace('+1-304-845-2727', '+1-325-947-0470')
    content = content.replace('(304) 000-0000', '(325) 000-0000')

    # Addresses
    content = content.replace('511 Fifth Street, Moundsville, WV 26041', '3546 Sherwood Way, San Angelo, TX 76901')
    content = content.replace('511 Fifth Street<br>Moundsville, WV 26041', '3546 Sherwood Way<br>San Angelo, TX 76901')
    content = content.replace('Serving Wheeling, WV &middot; Moundsville, WV', 'Serving San Angelo, TX')
    content = content.replace('Serving Wheeling &amp; Moundsville', 'Serving San Angelo, TX')
    
    content = content.replace("West Virginia's", "San Angelo's")
    content = content.replace("in West Virginia", "in San Angelo, TX")
    content = content.replace("– West Virginia", "– San Angelo, TX")
    content = content.replace("in WV", "in San Angelo, TX")
    
    content = content.replace("House of Polish WV", "House of Polish")
    content = content.replace("Golden Nail Spa WV", "Golden Nail, Spa")
    content = content.replace('"addressRegion": "WV"', '"addressRegion": "TX"')
    content = content.replace('q=West+Virginia', 'q=San+Angelo,+TX')
    content = content.replace('location map – West Virginia', 'location map – San Angelo, TX')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates applied.")
