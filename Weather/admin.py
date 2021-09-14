from django.contrib import admin
from .models import City

class cityadmin(admin.ModelAdmin):
    class Meta:
        model=City

admin.site.register(City,cityadmin)
