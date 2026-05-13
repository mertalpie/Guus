import re

def translate_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    
    for en, nl in replacements.items():
        content = content.replace(en, nl)
        
    with open(filepath, 'w') as f:
        f.write(content)

# Global replacements
global_replacements = {
    'Discover': 'Ontdek',
    'Dashboard': 'Dual-Dashboard',
    'Log in': 'Inloggen',
    'Join Haven': 'Word lid',
    '/ mo': '/ mnd',
    'Community Chat': 'Community Chat',
    'Explore all locations': 'Bekijk alle locaties',
    'Explore all': 'Bekijk alle',
    'Curated Long Stays': 'Geselecteerde Long Stays',
    'Hand-picked homes with thriving local communities across the globe.': 'Zorgvuldig geselecteerde woningen met bruisende lokale communities wereldwijd.',
    'Explore': 'Ontdekken',
    'Cities': 'Steden',
    'Communities': 'Communities',
    'How it works': 'Hoe het werkt',
    'Hosting': 'Verhuren',
    'List your home': 'Verhuur je woning',
    'Landlord Approval Flow': 'Verhuurder Goedkeuring',
    'Trust & Safety': 'Vertrouwen & Veiligheid',
    'Company': 'Bedrijf',
    'About Us': 'Over Ons',
    'Careers': 'Werken bij',
    'Contact': 'Contact',
    'Privacy': 'Privacy',
    'Terms': 'Voorwaarden',
    'Sitemap': 'Sitemap',
    'Revolutionizing long-term stays through community matching and safe subletting.': 'Een revolutie in long-term stays door community matching en veilige onderverhuur.'
}

# Index specific
index_replacements = {
    'Live anywhere.<br><span class="text-brand-sand italic">Belong everywhere.</span>': 'Woon overal.<br><span class="text-brand-sand italic">Voel je overal thuis.</span>',
    'The exclusive platform for stays of 1+ months. We match you with high-end homes and pro-actively connect you with neighbors who share your passions.': 'Het exclusieve platform voor verblijven van 1+ maanden. Wij matchen je met high-end woningen en verbinden je proactief met buren die jouw passies delen.',
    'Where do you want to live?': 'Waar wil je wonen?',
    'Find Matches': 'Vind Matches',
    'Interest Matching': 'Interesse Matching',
    'Verified Subletting': 'Geverifieerde Onderverhuur',
    '3 Tech Founders': '3 Tech Founders',
    'Live in this building': 'Wonen in dit gebouw',
    'More than just a place to sleep': 'Meer dan alleen een plek om te slapen',
    'We solve modern isolation and empty homes by combining smart matching with legal subletting tools.': 'Wij lossen moderne eenzaamheid en leegstand op door slimme matching te combineren met veilige onderverhuur.',
    'Community-First': 'Community-First',
    'Our algorithm connects you with neighborhoods and co-living spaces where people share your interests—from Padel to Tech startups.': 'Ons algoritme verbindt je met wijken en co-living spaces waar mensen jouw interesses delen—van Padel tot Tech startups.',
    'Long Stay Focus': 'Long Stay Focus',
    'Exclusively for stays of 1 month or longer. Settle in, unpack your bags, and actually become part of the local fabric.': 'Exclusief voor verblijven van 1 maand of langer. Pak je koffers uit en word echt onderdeel van de lokale cultuur.',
    'Safe Subletting': 'Veilig Onderverhuren',
    'Going abroad? Rent out your own place safely via our platform with automated landlord approval flows and premium insurance.': 'Ga je naar het buitenland? Verhuur je eigen woning veilig via ons platform met geautomatiseerde goedkeuring van de verhuurder en premium verzekeringen.'
}

translate_file('index.html', {**global_replacements, **index_replacements})
translate_file('dashboard.html', global_replacements)
translate_file('matching.html', global_replacements)
translate_file('listing.html', global_replacements)
translate_file('community-chat.html', global_replacements)

