from django.urls import path
from . import views
# from users.models.advanceuser import AdvanceUser  



urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('guest-login/', views.guest_login, name='guest_login'),
    path('success/', views.success_page, name='success_page'),  # Define success_page too
    path('advance-users/', views.show_advance_users, name='show_advance_users'),
]
