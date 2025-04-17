from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import translation
import time
from django.http import HttpResponse
import json
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

def home(request):
    """Home pagina view."""
    current_language = translation.get_language() or 'nl'
    
    # Probeer eerst de taalspecifieke template
    template_path = f'language/{current_language}/home.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        # Gebruik de standaard template als de taalspecifieke niet bestaat
        template_path = 'main/home.html'
    
    context = {
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def about(request):
    """About pagina view."""
    current_language = translation.get_language() or 'nl'
    
    # Probeer eerst de taalspecifieke template
    template_path = f'language/{current_language}/about.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        # Gebruik de standaard template als de taalspecifieke niet bestaat
        template_path = 'main/about.html'
    
    context = {
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def contact(request):
    """Contact pagina view."""
    current_language = translation.get_language() or 'nl'
    
    # Probeer eerst de taalspecifieke template
    template_path = f'language/{current_language}/contact.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        # Gebruik de standaard template als de taalspecifieke niet bestaat
        template_path = 'main/contact.html'
    
    context = {
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def logo_demo(request):
    """Logo demo pagina view."""
    current_language = translation.get_language() or 'nl'
    
    # Probeer eerst de taalspecifieke template
    template_path = f'language/{current_language}/logo_demo.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        # Gebruik de standaard template als de taalspecifieke niet bestaat
        template_path = 'main/logo_demo.html'
    
    context = {
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def select_language(request):
    """View for language selection."""
    if request.method == 'POST':
        # Process language combination and action selection
        selected_combination = request.POST.get('selected_combination', '')
        selected_action = request.POST.get('selected_action', '')
        
        if not selected_combination or not selected_action:
            messages.error(request, 'Selecteer alstublieft een taalcombinatie en actie.')
            
            # Bepaal de template op basis van de taal
            current_language = translation.get_language() or 'nl'
            template_path = f'language/{current_language}/select_language.html'
            
            # Fallback naar de standaard template als de taalspecifieke niet bestaat
            try:
                get_template(template_path)
            except:
                template_path = 'main/select_language.html'
            
            # Stel de titel in op basis van de taal
            if current_language == 'de':
                title = 'Sprache auswählen'
            elif current_language == 'en':
                title = 'Select Language'
            else:
                title = 'Selecteer Taal'
            
            context = {
                'title': title,
                'LANGUAGE_CODE': current_language
            }
            return render(request, template_path, context)
        
        # Store selections in session
        request.session['selected_combination'] = selected_combination
        request.session['selected_action'] = selected_action
        
        # Parse the language combination
        source_lang, target_lang = selected_combination.split('-')
        
        # Determine the redirect URL based on the action
        if selected_action == 'learn':
            # Redirect to learning page without message
            return redirect('main:learn')
        elif selected_action == 'type':
            # Redirect to typing page with message
            messages.success(request, f'U gaat nu {target_lang.upper()} overtypen vanuit {source_lang.upper()}!')
            return redirect('main:type')
        else:
            messages.error(request, 'Ongeldige actie geselecteerd.')
            
            # Bepaal de template op basis van de taal
            current_language = translation.get_language() or 'nl'
            template_path = f'language/{current_language}/select_language.html'
            
            # Fallback naar de standaard template als de taalspecifieke niet bestaat
            try:
                get_template(template_path)
            except:
                template_path = 'main/select_language.html'
            
            # Stel de titel in op basis van de taal
            if current_language == 'de':
                title = 'Sprache auswählen'
            elif current_language == 'en':
                title = 'Select Language'
            else:
                title = 'Selecteer Taal'
            
            context = {
                'title': title,
                'LANGUAGE_CODE': current_language
            }
            return render(request, template_path, context)
    
    # Bepaal de template op basis van de taal
    current_language = translation.get_language() or 'nl'
    template_path = f'language/{current_language}/select_language.html'
    
    # Fallback naar de standaard template als de taalspecifieke niet bestaat
    try:
        get_template(template_path)
    except:
        template_path = 'main/select_language.html'
    
    # Stel de titel in op basis van de taal
    if current_language == 'de':
        title = 'Sprache auswählen'
    elif current_language == 'en':
        title = 'Select Language'
    else:
        title = 'Selecteer Taal'
    
    context = {
        'title': title,
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def learn(request):
    """Learn pagina view."""
    current_language = translation.get_language() or 'nl'
    
    # Probeer eerst de taalspecifieke template
    template_path = f'language/{current_language}/learn.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        # Gebruik de standaard template als de taalspecifieke niet bestaat
        template_path = 'main/learn.html'
    
    # Haal de geselecteerde talen op uit de sessie of gebruik standaardwaarden
    source_lang = request.session.get('source_language', 'Dutch')
    target_lang = request.session.get('target_language', 'English')
    
    context = {
        'source_lang': source_lang,
        'target_lang': target_lang,
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def type(request):
    """Type pagina view."""
    current_language = translation.get_language() or 'nl'
    
    # Probeer eerst de taalspecifieke template
    template_path = f'language/{current_language}/type.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        # Gebruik de standaard template als de taalspecifieke niet bestaat
        template_path = 'main/type.html'
    
    # Haal de geselecteerde talen op uit de sessie of gebruik standaardwaarden
    source_lang = request.session.get('source_language', 'Dutch')
    target_lang = request.session.get('target_language', 'English')
    
    context = {
        'source_lang': source_lang,
        'target_lang': target_lang,
        'LANGUAGE_CODE': current_language
    }
    return render(request, template_path, context)

def set_language(request, language_code):
    """
    Set the user's language preference and redirect to the previous page.
    Debug: Print the language code to the console.
    """
    print(f"Changing language to: {language_code}")
    
    # Store the language preference in the session
    if language_code in [lang[0] for lang in settings.LANGUAGES]:
        request.session['django_language'] = language_code
        translation.activate(language_code)
    
    # Get the redirect URL from the request
    redirect_url = request.META.get('HTTP_REFERER', '/')
    
    # Add a parameter to indicate language change
    if '?' in redirect_url:
        redirect_url += f'&lang_changed={language_code}&t={int(time.time())}'
    else:
        redirect_url += f'?lang_changed={language_code}&t={int(time.time())}'
    
    print(f"Redirecting to: {redirect_url}")
    
    return redirect(redirect_url)

def force_dutch(request):
    """Forceert Nederlands als taal."""
    # Activeer Nederlands
    translation.activate('nl')
    
    # Sla de taal op in de sessie met beide sleutels voor consistentie
    request.session['django_language'] = 'nl'
    request.session['_language'] = 'nl'
    
    # Voeg een timestamp toe aan de redirect URL om caching te voorkomen
    next_url = request.META.get('HTTP_REFERER', '/')
    if '?' in next_url:
        next_url += f'&lang_changed=nl&t={int(time.time())}'
    else:
        next_url += f'?lang_changed=nl&t={int(time.time())}'
    
    # Redirect naar de vorige pagina of home
    response = redirect(next_url)
    response.set_cookie('django_language', 'nl', max_age=60*60*24*365)
    return response

def debug_language(request):
    """Debug functie die informatie over de huidige taalinstellingen toont."""
    # Verzamel informatie over de taalinstellingen
    debug_info = {
        'current_language': translation.get_language(),
        'session_django_language': request.session.get('django_language'),
        'session_underscore_language': request.session.get('_language'),
        'cookie_django_language': request.COOKIES.get('django_language'),
        'available_languages': [lang[0] for lang in settings.LANGUAGES],
        'middleware': settings.MIDDLEWARE,
    }
    
    # Toon deze informatie in een eenvoudige HTML-pagina
    html = f"""
    <html>
    <head>
        <title>Taal Debug Informatie</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            pre {{ background-color: #f0f0f0; padding: 15px; border-radius: 5px; }}
            .back-link {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>Taal Debug Informatie</h1>
        <pre>{json.dumps(debug_info, indent=4)}</pre>
        <div class="back-link">
            <a href="{request.META.get('HTTP_REFERER', '/')}">Terug naar vorige pagina</a>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)
