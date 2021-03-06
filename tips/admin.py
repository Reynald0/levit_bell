from django.contrib import admin
from .models import Tip

class TipAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'fecha_publicacion')

admin.site.register(Tip, TipAdmin)