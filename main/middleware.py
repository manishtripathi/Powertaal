from django.utils import translation
from django.conf import settings

class DefaultLanguageMiddleware:
    """Middleware om de standaardtaal in te stellen als er geen taal is geselecteerd."""
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Haal beschikbare taalcodes uit de settings
        available_languages = [lang[0] for lang in settings.LANGUAGES]
        
        # Controleer eerst de sessie voor de taal (check beide mogelijke sleutels)
        language_from_session = request.session.get('django_language') or request.session.get('_language')
        
        # Als er geen taal in de sessie is, controleer de cookie
        if not language_from_session:
            language_from_cookie = request.COOKIES.get('django_language')
            if language_from_cookie and language_from_cookie in available_languages:
                language_from_session = language_from_cookie
        
        # Als er een geldige taal is gevonden, activeer deze
        if language_from_session and language_from_session in available_languages:
            translation.activate(language_from_session)
            # Sla de taal op in beide sessie sleutels voor compatibiliteit
            request.session['django_language'] = language_from_session
            request.session['_language'] = language_from_session
        else:
            # Anders, activeer Nederlands als standaard
            translation.activate('nl')
            request.session['django_language'] = 'nl'
            request.session['_language'] = 'nl'
        
        response = self.get_response(request)
        
        # Zorg ervoor dat de taal ook in de cookie wordt opgeslagen
        if hasattr(request, 'session') and 'django_language' in request.session:
            response.set_cookie('django_language', request.session['django_language'], max_age=60*60*24*365)
        
        return response 