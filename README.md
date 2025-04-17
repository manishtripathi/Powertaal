# PowerTaal - Taalplatform

![PowerTaal Logo](static/img/brand-logo.png)

## Over PowerTaal

PowerTaal is een interactief taalplatform dat gebruikers helpt bij het leren en oefenen van verschillende talen. Het platform biedt een gebruiksvriendelijke omgeving waar gebruikers in hun eigen tempo kunnen leren door middel van herhaling, gevarieerde oefeningen en praktische toepassingen.

**Slogan:** VINGERSVLUG WOORDEN LEREN & SCHRIJVEN

## Functies

### Voor alle gebruikers (Standaard optie - Gratis)
- **Basiswoordenschat oefenen** zonder registratie
- **Meerdere talen** beschikbaar om te oefenen
- **Verschillende oefenmodi** voor effectief leren
- **Score bijhouden** aan het einde van elke oefensessie

### Voor premium gebruikers (Geavanceerde optie - €7,99)
- **Uitgebreide woordenschat** met meer woorden en zinnen
- **Zinsoefeningen** om complete zinnen te leren en oefenen
- **Artikelen & grammatica** oefenen met woorden en bijbehorende lidwoorden
- **Dictee-oefeningen** om luister- en schrijfvaardigheden te verbeteren
- **Persoonlijk dashboard** om voortgang bij te houden
- **Regelmatige updates** met nieuwe woorden en zinnen

## Technische details

### Projectstructuur
```
PowertaalDjango/
├── db.sqlite3                # SQLite database
├── manage.py                 # Django beheerscript
├── powertaal/                # Hoofdproject configuratie
├── main/                     # Hoofdapplicatie
│   ├── views.py              # Views voor de hoofdpagina's
│   ├── urls.py               # URL-configuratie
│   └── ...
├── users/                    # Gebruikersapplicatie
├── form/                     # Formulierapplicatie
├── static/                   # Statische bestanden (CSS, JS, afbeeldingen)
│   ├── css/
│   ├── js/
│   └── img/
└── templates/                # HTML-templates
    ├── base.html             # Basis template
    ├── includes/             # Herbruikbare template-onderdelen
    ├── main/                 # Templates voor hoofdapplicatie
    └── users/                # Templates voor gebruikersapplicatie
```

### Technologieën
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (ontwikkeling)
- **Hosting:** [Specificeer productieomgeving]

## Installatie

### Vereisten
- Python 3.8+
- Django 5.1+
- Overige afhankelijkheden (zie requirements.txt)

### Stappen
1. Clone de repository:
   ```
   git clone [repository-url]
   ```

2. Maak een virtuele omgeving aan en activeer deze:
   ```
   python -m venv venv
   source venv/bin/activate  # Op Windows: venv\Scripts\activate
   ```

3. Installeer de benodigde packages:
   ```
   pip install -r requirements.txt
   ```

4. Voer database migraties uit:
   ```
   python manage.py migrate
   ```

5. Start de ontwikkelingsserver:
   ```
   python manage.py runserver
   ```

6. Open de website in je browser:
   ```
   http://127.0.0.1:8000/
   ```

## Gebruik

### Standaard gebruikers
1. Bezoek de PowerTaal homepage
2. Klik op de "Start Nu" knop onder de Standaard optie
3. Selecteer de gewenste taal om te oefenen
4. Kies een oefenmodus en begin direct met leren

### Premium gebruikers
1. Bezoek de PowerTaal homepage
2. Klik op de "Inloggen" knop onder de Geavanceerde optie
3. Log in met je gegevens of registreer voor een nieuw account (€7,99)
4. Na het inloggen heb je toegang tot je persoonlijke dashboard

## Pagina's

- **Home:** Introductie van het platform met de twee hoofdopties
- **Over ons:** Informatie over PowerTaal en het team
- **Registreren:** Aanmeldpagina voor nieuwe gebruikers
- **Contact:** Contactformulier voor vragen en ondersteuning
- **Taalselectie:** Pagina om de gewenste taal te kiezen
- **Oefenpagina's:** Verschillende oefenmodi voor taalpraktijk
- **Gebruikershandleiding:** Uitgebreide handleiding voor gebruikers

## Onderhoud en ontwikkeling

### Nieuwe talen toevoegen
Om een nieuwe taal toe te voegen aan het platform:
1. Voeg de taal toe aan het taalselectiemenu
2. Maak de bijbehorende woordenlijsten en oefeningen aan
3. Test de nieuwe taal grondig voor publicatie

### Content bijwerken
Voor premium gebruikers worden maandelijks nieuwe woorden en zinnen toegevoegd:
1. Bereid nieuwe woordenlijsten voor
2. Voeg deze toe aan de database
3. Test de nieuwe content
4. Publiceer de updates

## Contact & Ondersteuning

- **E-mail:** support@powertaal.com
- **Contactformulier:** Beschikbaar op de contactpagina
- **Ondersteuningsteam:** Beschikbaar van maandag t/m vrijdag, 9:00-17:00 CET

## Licentie

[Specificeer licentie-informatie]

---

© PowerTaal. Alle rechten voorbehouden. 