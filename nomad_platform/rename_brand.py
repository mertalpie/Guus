import os

replacements = {
    'Haven.': 'WonenZonderGrenzen.',
    'Haven Platform': 'WonenZonderGrenzen Platform',
    'Haven Servicekosten': 'WonenZonderGrenzen Servicekosten',
    'Haven-leden': 'WonenZonderGrenzen-leden',
    'Haven': 'WonenZonderGrenzen' # Catch any remaining instances
}

for filename in ['index.html', 'dashboard.html', 'matching.html', 'listing.html', 'community-chat.html']:
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filename, 'w') as f:
        f.write(content)

print("Replacement complete.")
