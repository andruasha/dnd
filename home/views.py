from django.shortcuts import render
from home.forms import SpellForm


def index(request):
    return render(request, 'home/index.html')


def bestiary_find(request):
    return render(request, 'home/bestiary_find.html')


def bestiary_create(request):
    return render(request, 'home/bestiary_create.html')


def bestiary_delete(request):
    return render(request, 'home/bestiary_delete.html')


def items_find(request):
    return render(request, 'home/items_find.html')


def items_create(request):
    return render(request, 'home/items_create.html')


def items_delete(request):
    return render(request, 'home/items_delete.html')


def spells_find(request):
    if request.method == 'POST':
        form = SpellForm(data=request.POST)
        spell_level = request.POST['Spell_Level']
        school = request.POST['School']
        archetype = request.POST['Archetypes']
        print(spell_level)
    else:
        form = SpellForm()
    print('penis')
    context = {'form': form}
    return render(request, 'home/spells_find.html', context)


def spells_create(request):
    return render(request, 'home/spells_create.html')


def spells_delete(request):
    return render(request, 'home/spells_delete.html')