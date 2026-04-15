files = ['index.html', 'golden_nail_and_spa.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Cards list to modify
    replacements = [
        ('onclick="showPage(\'menu\')" aria-label="Nail services"', 'onclick="showPage(\'menu\', \'menu-nails\')" aria-label="Nail services"'),
        ('onclick="showPage(\'menu\')" aria-label="Manicure services"', 'onclick="showPage(\'menu\', \'menu-manicures\')" aria-label="Manicure services"'),
        ('onclick="showPage(\'menu\')" aria-label="Pedicure services"', 'onclick="showPage(\'menu\', \'menu-pedicures\')" aria-label="Pedicure services"'),
        ('onclick="showPage(\'menu\')" aria-label="Kid services"', 'onclick="showPage(\'menu\', \'menu-kids\')" aria-label="Kid services"'),
        ('onclick="showPage(\'menu\')" aria-label="Waxing services"', 'onclick="showPage(\'menu\', \'menu-waxing\')" aria-label="Waxing services"'),
        ('onclick="showPage(\'menu\')" aria-label="Eyelash extensions"', 'onclick="showPage(\'menu\', \'menu-eyelashes\')" aria-label="Eyelash extensions"')
    ]

    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Outer Div onClicks updated to use anchors!")
