from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += ('Pokeball', {'fields': ['pokeball']}),
admin.site.register(User, UserAdmin)