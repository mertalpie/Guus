with open('matching.html', 'r') as f:
    content = f.read()

replacements = {
    'Select your interests below to discover your tribe and find the perfect long-stay property.': 'Selecteer hieronder je interesses om je community te ontdekken en de perfecte long-stay woning te vinden.',
    'Nearby Resident': 'Buurtbewoner',
    'Coliving Hub': 'Coliving Hub',
    'Coliving Villa': 'Coliving Villa',
    'Expat Loft': 'Expat Loft',
}

for en, nl in replacements.items():
    content = content.replace(en, nl)

with open('matching.html', 'w') as f:
    f.write(content)

