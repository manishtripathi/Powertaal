from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('logo-demo/', views.logo_demo, name='logo-demo'),
    path('select-language/', views.select_language, name='select-language'),
    path('learn/', views.learn, name='learn'),
    path('type/', views.type, name='type'),
    path('set-language/<str:language_code>/', views.set_language, name='set_language'),
    path('force-dutch/', views.force_dutch, name='force_dutch'),
    path('debug-language/', views.debug_language, name='debug_language'),
] 