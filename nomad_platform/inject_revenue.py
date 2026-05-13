import re

html_to_inject = """
    <!-- Revenue Share Slide -->
    <section class="py-24 bg-brand-navy text-white relative overflow-hidden">
        <!-- Background decoration -->
        <div class="absolute right-0 top-0 w-96 h-96 bg-brand-sand opacity-5 rounded-full blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid lg:grid-cols-2 gap-16 items-center">
                
                <!-- Left Column -->
                <div>
                    <div class="flex items-center gap-4 mb-6">
                        <div class="w-8 h-px bg-brand-sand"></div>
                        <span class="text-brand-sand font-bold text-xs tracking-widest uppercase">Revenue Share Systeem</span>
                    </div>
                    <h2 class="font-display text-4xl lg:text-6xl font-bold mb-6">Jouw woning werkt <span class="italic text-brand-sand font-normal">voor jou</span></h2>
                    <p class="text-gray-300 text-lg mb-12 max-w-lg">
                        Vertrek naar het buitenland en laat je woning rendement genereren. Volledig legaal, volledig geautomatiseerd.
                    </p>
                    
                    <div class="space-y-8">
                        <div class="flex gap-6">
                            <div class="font-display text-4xl font-bold text-brand-sand">01</div>
                            <div>
                                <h4 class="font-bold text-lg mb-1">Verhuurder-toestemming regelen</h4>
                                <p class="text-sm text-gray-400">Wij begeleiden het proces voor toestemming van je verhuurder of corporatie. Inclusief standaard-overeenkomsten die door meer dan 120 corporaties zijn goedgekeurd.</p>
                            </div>
                        </div>
                        <div class="flex gap-6">
                            <div class="font-display text-4xl font-bold text-brand-sand">02</div>
                            <div>
                                <h4 class="font-bold text-lg mb-1">Listing activeren</h4>
                                <p class="text-sm text-gray-400">Upload foto's, stel je prijs in en kies je beschikbaarheidsperiode. Je listing gaat automatisch live zodra jij vertrekdatum bevestigt.</p>
                            </div>
                        </div>
                        <div class="flex gap-6">
                            <div class="font-display text-4xl font-bold text-brand-sand">03</div>
                            <div>
                                <h4 class="font-bold text-lg mb-1">Gescreende huurders</h4>
                                <p class="text-sm text-gray-400">Alleen geverifieerde Haven-leden kunnen jouw woning huren. Automatische huurinkasso en schade-depositobeheer.</p>
                            </div>
                        </div>
                        <div class="flex gap-6">
                            <div class="font-display text-4xl font-bold text-brand-sand">04</div>
                            <div>
                                <h4 class="font-bold text-lg mb-1">Passief inkomen genereren</h4>
                                <p class="text-sm text-gray-400">Maandelijkse uitbetalingen op je rekening. Gemiddeld dekt de huurinkomst 60-100% van jouw eigen verblijfskosten in het buitenland.</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right Column: Calculator Widget -->
                <div class="bg-[#1A2837] rounded-xl border border-gray-700 shadow-2xl overflow-hidden p-8">
                    <p class="text-brand-sand text-xs font-bold tracking-widest uppercase mb-4">Voorbeeldberekening</p>
                    <h3 class="font-display text-2xl font-bold mb-8">Jan de Vries &middot; Amsterdam &harr; Bali</h3>
                    
                    <div class="space-y-4 text-sm text-gray-300">
                        <div class="flex justify-between items-center pb-4 border-b border-gray-700">
                            <span>Huurwaarde Amsterdam</span>
                            <span class="font-bold text-white">&euro;1.850 / mnd</span>
                        </div>
                        <div class="flex justify-between items-center pb-4 border-b border-gray-700">
                            <span>Platform fee (12%)</span>
                            <span class="font-bold text-white">&minus; &euro;222</span>
                        </div>
                        <div class="flex justify-between items-center pb-4 border-b border-gray-700">
                            <span>Netto inkomsten</span>
                            <span class="font-bold text-brand-success text-base">&euro;1.628 / mnd</span>
                        </div>
                        <div class="flex justify-between items-center pb-4 border-b border-gray-700">
                            <span>Verblijf Bali (coliving)</span>
                            <span class="font-bold text-white">&euro;950 / mnd</span>
                        </div>
                        <div class="flex justify-between items-center pt-2 mb-8">
                            <span>Netto voordeel per maand</span>
                            <span class="font-bold text-brand-success text-base">+ &euro;678</span>
                        </div>
                    </div>
                    
                    <div class="mt-8 bg-black bg-opacity-20 rounded-lg p-5 border border-gray-700">
                        <p class="text-brand-sand text-xs font-bold tracking-widest uppercase mb-2">Conclusie</p>
                        <p class="text-sm text-gray-300 leading-relaxed">
                            Jan verdient &euro;678/mnd extra terwijl hij in Bali woont. Zijn verblijf kost hem effectief nul.
                        </p>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

with open('index.html', 'r') as f:
    content = f.read()

# Insert before the footer
if "<!-- Footer -->" in content:
    content = content.replace("<!-- Footer -->", html_to_inject + "\n    <!-- Footer -->")
else:
    print("Footer comment not found in index.html!")

with open('index.html', 'w') as f:
    f.write(content)

