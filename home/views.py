from home.forms import BestiaryFindForm, BestiaryDeleteForm, BestiaryCreateForm
from home.forms import ItemsFindForm, ItemsDeleteForm, ItemsCreateForm
from home.forms import SpellFindForm
from django.shortcuts import render, HttpResponseRedirect
from home.models import Author, Items, Item_Type as Item_Types
from home.models import Size, Species, Worldview, Armor, Language, Habitat
from home.models import Item_Type as Items_Type
from home.models import School, Archetypes as Archetype
from home.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from home.sqlqueries import func


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home:index'))
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
    sizes = Size.objects.all()
    specieses = Species.objects.all()
    worldviews = Worldview.objects.all()
    armors = Armor.objects.all()
    languages = Language.objects.all()
    habitats = Habitat.objects.all()

    context = {'form': form,
               'authors': authors,
               'sizes': sizes,
               'specieses': specieses,
               'worldviews': worldviews,
               'armors': armors,
               'languages': languages,
               'habitats': habitats, }

    return render(request, 'home/bestiary_find.html', context)


@login_required(login_url='home:login')
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
    sizes = Size.objects.all()
    specieses = Species.objects.all()
    worldviews = Worldview.objects.all()
    armors = Armor.objects.all()
    languages = Language.objects.all()
    habitats = Habitat.objects.all()

    context = {'form': form,
               'authors': authors,
               'sizes': sizes,
               'specieses': specieses,
               'worldviews': worldviews,
               'armors': armors,
               'languages': languages,
               'habitats': habitats, }

    return render(request, 'home/bestiary_create.html', context)


@login_required(login_url='home:login')
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
    sizes = Size.objects.all()
    specieses = Species.objects.all()
    worldviews = Worldview.objects.all()
    armors = Armor.objects.all()
    languages = Language.objects.all()
    habitats = Habitat.objects.all()

    context = {'form': form,
               'authors': authors,
               'sizes': sizes,
               'specieses': specieses,
               'worldviews': worldviews,
               'armors': armors,
               'languages': languages,
               'habitats': habitats, }

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
    types = Items_Type.objects.all()

    context = {'form': form,
               'authors': authors,
               'types': types, }

    return render(request, 'home/items_find.html', context)


@login_required(login_url='home:login')
def items_create(request):
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        if form.is_valid():
            Item_ID = request.POST['Item_ID']
            Item_Type = request.POST['Item_Type']

            item_type = Item_Types.objects.get(pk=Item_Type)

            Item_Subtype = request.POST['Item_Subtype']
            Item_Rarity = request.POST['Item_Rarity']
            Item_Setting = request.POST['Item_Setting']
            Item_Price = request.POST['Item_Price']
            Item_Description = request.POST['Item_Description']

            Items.objects.create(Item_ID=Item_ID,
                                 Item_Type=item_type,
                                 Item_Subtype=Item_Subtype,
                                 Item_Rarity=Item_Rarity,
                                 Item_Setting=Item_Setting,
                                 Item_Author_id=request.user.pk,
                                 Item_Price=Item_Price,
                                 Item_Description=Item_Description)

        else:
            print('error')
    else:
        form = ItemsCreateForm()

    func()
    authors = Author.objects.all()
    types = Items_Type.objects.all()

    context = {'form': form,
               'authors': authors,
               'types': types, }

    return render(request, 'home/items_create.html', context)


@login_required(login_url='home:login')
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
        form = ItemsDeleteForm()

    authors = Author.objects.all()
    types = Items_Type.objects.all()

    context = {'form': form,
               'authors': authors,
               'types': types, }

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
    schools = School.objects.all()
    archetypes = Archetype.objects.all()

    context = {'form': form,
               'authors': authors,
               'schools': schools,
               'archetypes': archetypes, }

    return render(request, 'home/spells_find.html', context)


@login_required(login_url='home:login')
def spells_create(request):
    if request.method == 'POST':
        form = SpellFindForm(data=request.POST)
        Spell_ID = request.POST['Spell_ID']
        Spell_Type = request.POST['Spell_Type']
        Spell_Rarity = request.POST['Spell_Rarity']
        Spell_Level = request.POST['Spell_Level']
        Archetypes = request.POST['Archetypes']
        Spell_Author = request.POST['Spell_Author']

        print(Spell_ID, Spell_Level, Archetypes, Spell_Author)
    else:
        form = SpellFindForm()

    authors = Author.objects.all()
    schools = School.objects.all()
    archetypes = Archetype.objects.all()

    context = {'form': form,
               'authors': authors,
               'schools': schools,
               'archetypes': archetypes, }

    return render(request, 'home/spells_create.html', context)


@login_required(login_url='home:login')
def spells_delete(request):
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
    schools = School.objects.all()
    archetypes = Archetype.objects.all()

    context = {'form': form,
               'authors': authors,
               'schools': schools,
               'archetypes': archetypes, }

    return render(request, 'home/spells_delete.html', context)