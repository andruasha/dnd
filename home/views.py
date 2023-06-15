from home.forms import BestiaryFindForm, BestiaryDeleteForm, BestiaryCreateForm
from home.forms import ItemsFindForm, ItemsDeleteForm, ItemsCreateForm
from home.forms import SpellFindForm
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
    if request.method == 'POST':
        form = BestiaryCreateForm(data=request.POST)
        Bestiary_ID = request.POST['Bestiary_ID']
        Size_ID = request.POST['Size_ID']
        Species_ID = request.POST['Species_ID']
        Worldview_ID = request.POST['Worldview_ID']
        Danger = request.POST['Danger']
        Bestiary_Author = request.POST['Bestiary_Author']
        Language_ID = request.POST['Language_ID']
        Habitat_ID = request.POST['Habitat_ID']
        Hits = request.POST['Hits']
        Armor_ID = request.POST['Armor_ID']

        print(Bestiary_ID)
    else:
        form = BestiaryFindForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/bestiary_find.html', context)


def bestiary_create(request):
    if request.method == 'POST':
        form = BestiaryCreateForm(data=request.POST)
        Bestiary_ID = request.POST['Bestiary_ID']
        Size_ID = request.POST['Size_ID']
        Species_ID = request.POST['Species_ID']
        Speed = request.POST['Speed']
        Worldview_ID = request.POST['Worldview_ID']
        Danger = request.POST['Danger']
        Bestiary_Author = request.POST['Bestiary_Author']
        Language_ID = request.POST['Language_ID']
        Habitat_ID = request.POST['Habitat_ID']
        Hits = request.POST['Hits']
        Armor_ID = request.POST['Armor_ID']
        Characteristics = request.POST['Characteristics']
        Resistance_Damage = request.POST['Resistance_Damage']
        Immunity_Damage = request.POST['Immunity_Damage']
        Skills = request.POST['Skills']
        Description = request.POST['Description']

        print(Bestiary_ID)
    else:
        form = BestiaryCreateForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/bestiary_create.html', context)


def bestiary_delete(request):
    if request.method == 'POST':
        form = BestiaryCreateForm(data=request.POST)
        Bestiary_ID = request.POST['Bestiary_ID']
        Size_ID = request.POST['Size_ID']
        Species_ID = request.POST['Species_ID']
        Worldview_ID = request.POST['Worldview_ID']
        Danger = request.POST['Danger']
        Bestiary_Author = request.POST['Bestiary_Author']
        Language_ID = request.POST['Language_ID']
        Habitat_ID = request.POST['Habitat_ID']
        Hits = request.POST['Hits']
        Armor_ID = request.POST['Armor_ID']

        print(Bestiary_ID)
    else:
        form = BestiaryDeleteForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/bestiary_delete.html', context)


def items_find(request):
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        Item_ID = request.POST['Item_ID']
        Item_Type = request.POST['Item_Type']
        Item_Rarity = request.POST['Item_Rarity']
        Item_Setting = request.POST['Item_Setting']
        Item_Author = request.POST['Item_Author']
        Item_Price = request.POST['Item_Price']

        print(Item_ID)
    else:
        form = ItemsFindForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/items_find.html', context)


def items_create(request):
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        Item_ID = request.POST['Item_ID']
        Item_Type = request.POST['Item_Type']
        Item_Rarity = request.POST['Item_Rarity']
        Item_Setting = request.POST['Item_Setting']
        Item_Author = request.POST['Item_Author']
        Item_Price = request.POST['Item_Price']
        Item_Description = request.POST['Item_Description']

        print(Item_ID)
    else:
        form = ItemsCreateForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/items_create.html', context)


def items_delete(request):
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        Item_ID = request.POST['Item_ID']
        Item_Type = request.POST['Item_Type']
        Item_Rarity = request.POST['Item_Rarity']
        Item_Setting = request.POST['Item_Setting']
        Item_Author = request.POST['Item_Author']
        Item_Price = request.POST['Item_Price']

        print(Item_ID)
    else:
        form = ItemsCreateForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/items_delete.html', context)


def spells_find(request):
    if request.method == 'POST':
        form = SpellFindForm(data=request.POST)
        Spell_ID = request.POST['Spell_ID']
        Spell_Level = request.POST['Spell_Level']
        Archetypes = request.POST['Archetypes']
        Spell_Author = request.POST['Spell_Author']

        print(Spell_ID, Spell_Level, Archetypes, Spell_Author)
    else:
        form = SpellFindForm()
    authors = Author.objects.all()
    context = {'form': form, 'authors': authors}
    return render(request, 'home/spells_find.html', context)


def spells_create(request):
    return render(request, 'home/spells_create.html')


def spells_delete(request):
    return render(request, 'home/spells_delete.html')