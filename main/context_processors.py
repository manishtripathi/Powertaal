from django.utils import translation

def language_context(request):
    """Add language information to the template context."""
    current_language = translation.get_language()
    if not current_language:
        current_language = 'nl'  # Default to Dutch
    
    return {
        'CURRENT_LANGUAGE': current_language,
        'LANGUAGE_CODE': current_language,
        'IS_DUTCH': current_language == 'nl',
        'IS_ENGLISH': current_language == 'en',
        'IS_GERMAN': current_language == 'de',
        'IS_ARABIC': current_language == 'ar',
    } 