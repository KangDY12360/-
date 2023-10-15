# pokemon/admin.py
from django.contrib import admin
from .models import Pokemon

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'ability', 'evolution')  # 여기서 evolution 추가
    search_fields = ('name', 'evolution')  # 여기서도 evolution 추가

admin.site.register(Pokemon, PokemonAdmin)
