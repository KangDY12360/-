# pokemon/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pokemon



def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    selected_pokemon = None
    evolution_pokemon = None

    if 'selected_pokemon' in request.GET:
        selected_pokemon_id = request.GET['selected_pokemon']
        selected_pokemon = get_object_or_404(Pokemon, id=selected_pokemon_id)

        # Check if the selected Pokemon has an evolution
        evolution_pokemon_name = selected_pokemon.evolution
        if evolution_pokemon_name:
            evolution_pokemon = get_object_or_404(Pokemon, name=evolution_pokemon_name)

    return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemons, 'selected_pokemon': selected_pokemon, 'evolution_pokemon': evolution_pokemon})
