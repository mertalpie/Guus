import os

replacements = {
    # listing.html specific
    'Back': 'Terug',
    'My Dual-Dashboard': 'Mijn Dual-Dashboard',
    '8 Private Suites • Shared Workspaces • Rooftop Terrace': '8 Privé Suites • Gedeelde Werkplekken • Dakterras',
    'Great Match for You!': 'Perfecte Match voor Jou!',
    "Based on your interests, you'll love it here. The community is highly active in areas you care about.": "Gebaseerd op jouw interesses ga je het hier fantastisch vinden. De community is erg actief in de dingen die jij leuk vindt.",
    'Weekly Padel Matches': 'Wekelijkse Padel Wedstrijden',
    'About this home': 'Over deze woning',
    'A premium coliving space focused on shared workspaces, networking, and surfing. Enjoy the high-end design, warm sand tones, and natural light in your private suite.': 'Een premium coliving space gericht op gedeelde werkplekken, netwerken en surfen. Geniet van het high-end design, warme zandtinten en natuurlijk licht in je privé suite.',
    'The Nomads Villa is designed for professionals who want to be productive during the day and social in the evening. Our state-of-the-art coworking area features Herman Miller chairs, ultra-fast fiber internet, and soundproof phone booths.': 'De Nomads Villa is ontworpen voor professionals die overdag productief willen zijn en \'s avonds sociaal. Onze state-of-the-art coworking area beschikt over Herman Miller stoelen, razendsnel glasvezel internet en geluiddichte telefooncellen.',
    'Every Friday evening, the community gathers on the rooftop terrace for sunset drinks overlooking the Tagus river.': 'Elke vrijdagavond komt de community samen op het dakterras voor een borrel bij zonsondergang met uitzicht op de rivier de Taag.',
    'What this place offers': 'Wat deze plek biedt',
    'Dedicated Workspace': 'Eigen Werkplek',
    'Gigabit WiFi': 'Gigabit WiFi',
    'Weekly Cleaning': 'Wekelijkse Schoonmaak',
    'Premium Coffee': 'Premium Koffie',
    'Rooftop Terrace': 'Dakterras',
    'Washer & Dryer': 'Wasmachine & Droger',
    '/ mndnth': '/ mnd',
    'Move-in': 'Check-in',
    'Move-out': 'Check-out',
    'Guests': 'Gasten',
    '1 Resident': '1 Bewoner',
    'Request to Book': 'Aanvraag tot Boeken',
    "You won't be charged yet. Requires Host Approval.": 'Er worden nog geen kosten in rekening gebracht. Vereist goedkeuring van de verhuurder.',
    'x 3 months': 'x 3 maanden',
    'Haven Service Fee': 'Haven Servicekosten',
    'Total': 'Totaal',

    # index.html and tags
    '>Art<': '>Kunst<',
    '>Surfing<': '>Surfen<',
    '>Music<': '>Muziek<',
    '>Sailing<': '>Zeilen<',
    '>Gastronomy<': '>Gastronomie<',
    '>Coffee<': '>Koffie<',
    '>Hiking<': '>Wandelen<',
    '>Fashion<': '>Mode<',
    '>Architecture<': '>Architectuur<',
    '>Cycling<': '>Fietsen<',
    '>History<': '>Geschiedenis<',
    '>Photography<': '>Fotografie<',
    '>Literature<': '>Literatuur<',
    '>Crafts<': '>Ambachten<',
    
    'High-End Expat Loft': 'Luxe Expat Loft',
    'Kreuzberg Creative Space': 'Kreuzberg Creatieve Space',
    'Nordic Minimalist Flat': 'Noords Minimalistisch Appartement',
    'Historic Trastevere Loft': 'Historische Trastevere Loft',
    'Le Marais Artist Studio': 'Le Marais Kunstenaarsstudio',

    'Verified Member': 'Geverifieerd Lid',
    
    # Community Chat
    'Type your message...': 'Typ je bericht...',
    'Send': 'Verstuur',
    'Start a conversation': 'Start een gesprek',
    'No messages yet': 'Nog geen berichten'
}

for filename in ['index.html', 'dashboard.html', 'matching.html', 'listing.html', 'community-chat.html']:
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    for en, nl in replacements.items():
        content = content.replace(en, nl)
        
    with open(filename, 'w') as f:
        f.write(content)

