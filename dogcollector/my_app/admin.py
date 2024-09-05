from django.contrib import admin

from .models import Dog, Vaccine

admin.site.register(Dog)
admin.site.register(Vaccine)