from django.contrib import admin

# Register your models here.

from .models.advanceuser import AdvanceUser

admin.site.register(AdvanceUser)
