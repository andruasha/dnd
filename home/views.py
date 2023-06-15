from home.forms import SpellForm
from django.shortcuts import render, HttpResponseRedirect
from home.models import Author
from home.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'home/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:registration'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'home/registration.html', context)


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
        Spell_ID = request.POST['Spell_ID']
        Spell_Level = request.POST['Spell_Level']
        Archetypes = request.POST['Archetypes']
        Spell_Author = request.POST['Spell_Author']

        print(Spell_ID, Spell_Level, Archetypes, Spell_Author)
    else:
        form = SpellForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/spells_find.html', context)


def spells_create(request):
    return render(request, 'home/spells_create.html')


def spells_delete(request):
    return render(request, 'home/spells_delete.html')