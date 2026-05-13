def translate_file(filepath, replacements):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        for en, nl in replacements.items():
            content = content.replace(en, nl)
            
        with open(filepath, 'w') as f:
            f.write(content)
    except FileNotFoundError:
        print(f"{filepath} not found.")

replacements = {
    'Book Now': 'Boek Nu',
    'Message Host': 'Bericht Verhuurder',
    'About this space': 'Over deze ruimte',
    'Amenities': 'Voorzieningen',
    'Reviews': 'Beoordelingen',
    'Hosted by': 'Verhuurd door',
    'Similar Listings': 'Vergelijkbare Woningen',
    'Verified Host': 'Geverifieerde Verhuurder',
    'Contact Host': 'Neem Contact Op',
    'Check availability': 'Controleer beschikbaarheid',
    'Location': 'Locatie',
    'Description': 'Beschrijving',
    'House Rules': 'Huisregels',
    'Cancellation Policy': 'Annuleringsvoorwaarden',
    'Type your message...': 'Typ je bericht...',
    'Send': 'Verstuur',
    'Community Chat': 'Community Chat',
    'Concierge': 'Conciërge',
    'Online': 'Online',
    'Members': 'Leden',
    'Search...': 'Zoeken...',
    'Join': 'Deelnemen',
    'Events': 'Evenementen',
    'New': 'Nieuw',
    'Settings': 'Instellingen',
    'Profile': 'Profiel',
    'Log out': 'Uitloggen',
    'Start a conversation': 'Start een gesprek',
    'No messages yet': 'Nog geen berichten'
}

translate_file('listing.html', replacements)
translate_file('community-chat.html', replacements)

