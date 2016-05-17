from django.contrib import admin
from .models import Tip

class TipAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'no_texto')

admin.site.register(Tip, TipAdmin)
