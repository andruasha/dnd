from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

from home.forms import UserLoginForm, UserRegistrationForm
from home.forms import BestiaryFindForm, BestiaryDeleteForm, BestiaryCreateForm
from home.forms import ItemsFindForm, ItemsDeleteForm, ItemsCreateForm
from home.forms import SpellFindForm, SpellDeleteForm, SpellCreateForm

from home.models import Author, Bestiary, Spells, Items
from home.models import Item_Type
from home.models import Size, Species, Worldview, Armor, Language, Habitat
from home.models import School, Archetypes


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

        filters = Q()
        if Bestiary_ID:
            filters &= Q(Bestiary_ID__startswith=Bestiary_ID)

        if Size_ID:
            filters &= Q(Size_ID=Size_ID)

        if Species_ID:
            filters &= Q(Species_ID=Species_ID)

        if Worldview_ID:
            filters &= Q(Worldview_ID=Worldview_ID)

        if Danger:
            filters &= Q(Danger=Danger)

        if Bestiary_Author:
            filters &= Q(Bestiary_Author=Bestiary_Author)

        if Language_ID:
            filters &= Q(Language_ID=Language_ID)

        if Habitat_ID:
            filters &= Q(Habitat_ID=Habitat_ID)

        if Hits:
            filters &= Q(Hits=Hits)

        if Armor_ID:
            filters &= Q(Armor_ID=Armor_ID)

        results = Bestiary.objects.filter(filters)

    else:
        form = BestiaryFindForm()
        results = None

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
               'habitats': habitats,
               'results': results, }

    return render(request, 'home/bestiary_find.html', context)


def bestiary_detail(request, bestiary_id):
    bestiary = get_object_or_404(Bestiary, Bestiary_ID=bestiary_id)
    context = {'bestiary': bestiary}
    return render(request, 'home/bestiary_detail.html', context)


@login_required(login_url='home:login')
def bestiary_create(request):
    status = None
    if request.method == 'POST':
        form = BestiaryCreateForm(data=request.POST)
        Bestiary_ID = request.POST['Bestiary_ID']
        Size_ID = request.POST['Size_ID']
        Species_ID = request.POST['Species_ID']
        Speed = request.POST['Speed']
        Worldview_ID = request.POST['Worldview_ID']
        Danger = request.POST['Danger']
        Language_ID = request.POST['Language_ID']
        Habitat_ID = request.POST['Habitat_ID']
        Hits = request.POST['Hits']
        Armor_ID = request.POST['Armor_ID']
        Characteristics = request.POST['Characteristics']
        Resistance_Damage = request.POST['Resistance_Damage']
        Immunity_Damage = request.POST['Immunity_Damage']
        Skills = request.POST['Skills']
        Description = request.POST['Description']

        try:
            size_id = Size.objects.get(pk=Size_ID)
            species_id = Species.objects.get(pk=Species_ID)
            worldview_id = Worldview.objects.get(pk=Worldview_ID)
            armor_id = Armor.objects.get(pk=Armor_ID)
            language_id = Language.objects.get(pk=Language_ID)
            habitat_id = Habitat.objects.get(pk=Habitat_ID)

            if Bestiary_ID and size_id and species_id and worldview_id and armor_id and Hits and Speed and language_id and Characteristics and habitat_id and Danger:
                Bestiary.objects.create(Bestiary_ID = Bestiary_ID,
                                        Bestiary_Author_id=request.user.pk,
                                        Size_ID = size_id,
                                        Species_ID = species_id,
                                        Speed = Speed,
                                        Worldview_ID = worldview_id,
                                        Danger = Danger,
                                        Language_ID = language_id,
                                        Habitat_ID = habitat_id,
                                        Hits = Hits,
                                        Armor_ID = armor_id,
                                        Characteristics = Characteristics,
                                        Resistance_Damage = Resistance_Damage,
                                        Immunity_Damage = Immunity_Damage,
                                        Skills = Skills,
                                        Description = Description, )
                status = 'Ok'
            else:
                raise ValueError('Error')
        except:
            status = 'Error'

    else:
        form = BestiaryCreateForm()

    sizes = Size.objects.all()
    specieses = Species.objects.all()
    worldviews = Worldview.objects.all()
    armors = Armor.objects.all()
    languages = Language.objects.all()
    habitats = Habitat.objects.all()

    context = {'form': form,
               'sizes': sizes,
               'specieses': specieses,
               'worldviews': worldviews,
               'armors': armors,
               'languages': languages,
               'habitats': habitats,
               'status': status, }

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
        Language_ID = request.POST['Language_ID']
        Habitat_ID = request.POST['Habitat_ID']
        Hits = request.POST['Hits']
        Armor_ID = request.POST['Armor_ID']

        filter_params = {}

        if Bestiary_ID:
            filter_params['Bestiary_ID'] = Bestiary_ID

        if Size_ID:
            filter_params['Size_ID'] = Size_ID

        if Species_ID:
            filter_params['Species_ID'] = Species_ID

        if Worldview_ID:
            filter_params['Worldview_ID'] = Worldview_ID

        if Danger:
            filter_params['Danger'] = Danger

        if Language_ID:
            filter_params['Language_ID'] = Language_ID

        if Habitat_ID:
            filter_params['Habitat_ID'] = Habitat_ID

        if Hits:
            filter_params['Hits'] = Hits

        if Armor_ID:
            filter_params['Armor_ID'] = Armor_ID

        filter_params['Bestiary_Author_id'] = request.user.pk

        if len(filter_params)>1:
            try:
                Bestiary.objects.filter(**filter_params).delete()
                status = 'Ok'
            except:
                status = 'Error'
        else:
            status = 'Nothing'

    else:
        form = BestiaryDeleteForm()
        status = 'Nothing'

    sizes = Size.objects.all()
    specieses = Species.objects.all()
    worldviews = Worldview.objects.all()
    armors = Armor.objects.all()
    languages = Language.objects.all()
    habitats = Habitat.objects.all()

    context = {'form': form,
               'sizes': sizes,
               'specieses': specieses,
               'worldviews': worldviews,
               'armors': armors,
               'languages': languages,
               'habitats': habitats,
               'status': status, }

    return render(request, 'home/bestiary_delete.html', context)


def items_find(request):
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        Item_ID = request.POST['Item_ID']
        Item_Type_ID = request.POST['Item_Type']
        Item_Rarity = request.POST['Item_Rarity']
        Item_Setting = request.POST['Item_Setting']
        Item_Author = request.POST['Item_Author']
        Item_Price = request.POST['Item_Price']

        filters = Q()
        if Item_ID:
            filters &= Q(Item_ID__startswith=Item_ID)

        if Item_Type_ID:
            filters &= Q(Item_Type=Item_Type_ID)

        if Item_Rarity:
            filters &= Q(Item_Rarity=Item_Rarity)

        if Item_Setting:
            filters &= Q(Item_Setting=Item_Setting)

        if Item_Author:
            filters &= Q(Item_Author=Item_Author)

        if Item_Price:
            filters &= Q(Item_Price=Item_Price)

        results = Items.objects.filter(filters)
    else:
        form = ItemsFindForm()
        results = None

    authors = Author.objects.all()
    types = Item_Type.objects.all()

    context = {'form': form,
               'authors': authors,
               'types': types,
               'results': results, }

    return render(request, 'home/items_find.html', context)


def item_detail(request, item_id):
    item = get_object_or_404(Items, Item_ID=item_id)
    context = {'item': item}
    return render(request, 'home/item_detail.html', context)


@login_required(login_url='home:login')
def items_create(request):
    status = None
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        Item_ID = request.POST['Item_ID']
        Item_Type_ID = request.POST['Item_Type']
        Item_Subtype = request.POST['Item_Subtype']
        Item_Rarity = request.POST['Item_Rarity']
        Item_Setting = request.POST['Item_Setting']
        Item_Price = request.POST['Item_Price']
        Item_Description = request.POST['Item_Description']

        try:
            item_type = Item_Type.objects.get(pk=Item_Type_ID)
            if Item_ID and item_type and Item_Rarity:
                Items.objects.create(Item_ID=Item_ID,
                                     Item_Type=item_type,
                                     Item_Subtype=Item_Subtype,
                                     Item_Rarity=Item_Rarity,
                                     Item_Setting=Item_Setting,
                                     Item_Author_id=request.user.pk,
                                     Item_Price=Item_Price,
                                     Item_Description=Item_Description)
                status = 'Ok'
            else:
                raise ValueError('Error')
        except:
            status = 'Error'
    else:
        form = ItemsCreateForm()

    types = Item_Type.objects.all()

    context = {'form': form,
               'types': types,
               'status': status, }

    return render(request, 'home/items_create.html', context)


@login_required(login_url='home:login')
def items_delete(request):
    if request.method == 'POST':
        form = ItemsCreateForm(data=request.POST)
        Item_ID = request.POST['Item_ID']
        Item_Type_ID = request.POST['Item_Type']
        Item_Rarity = request.POST['Item_Rarity']
        Item_Setting = request.POST['Item_Setting']
        Item_Price = request.POST['Item_Price']

        filter_params = {}

        if Item_ID:
            filter_params['Item_ID'] = Item_ID

        if Item_Type_ID:
            filter_params['Item_Type'] = Item_Type_ID

        if Item_Rarity:
            filter_params['Item_Rarity'] = Item_Rarity

        if Item_Setting:
            filter_params['Item_Setting'] = Item_Setting

        if Item_Price:
            filter_params['Item_Price'] = Item_Price

        filter_params['Item_Author_id'] = request.user.pk

        if len(filter_params)>1:
            try:
                Items.objects.filter(**filter_params).delete()
                status = 'Ok'
            except:
                status = 'Error'
        else:
            status = 'Nothing'

    else:
        form = ItemsDeleteForm()
        status = 'Nothing'

    types = Item_Type.objects.all()

    context = {'form': form,
               'types': types,
               'status': status, }

    return render(request, 'home/items_delete.html', context)


def spells_find(request):
    results = None
    if request.method == 'POST':
        form = SpellFindForm(data=request.POST)
        Spell_ID = request.POST['Spell_ID']
        Spell_Level = request.POST['Spell_Level']
        School_ID = request.POST['School']
        Archetypes_ID = request.POST['Archetypes']
        Spell_Author = request.POST['Spell_Author']

        filters = Q()
        if Spell_ID:
            filters &= Q(Spell_ID__startswith=Spell_ID)

        if Spell_Level:
            filters &= Q(Spell_Level=Spell_Level)

        if School_ID:
            filters &= Q(School=School_ID)

        if Archetypes_ID:
            filters &= Q(Archetypes=Archetypes_ID)

        if Spell_Author:
            filters &= Q(Spell_Author=Spell_Author)

        results = Spells.objects.filter(filters)

    else:
        form = SpellFindForm()

    authors = Author.objects.all()
    schools = School.objects.all()
    archetypes = Archetypes.objects.all()

    context = {'form': form,
               'authors': authors,
               'schools': schools,
               'archetypes': archetypes,
               'results': results, }

    return render(request, 'home/spells_find.html', context)


def spell_detail(request, spell_id):
    spell = get_object_or_404(Spells, Spell_ID=spell_id)
    context = {'spell': spell}
    return render(request, 'home/spell_detail.html', context)


@login_required(login_url='home:login')
def spells_create(request):
    status = None
    if request.method == 'POST':
        form = SpellFindForm(data=request.POST)
        Spell_ID = request.POST['Spell_ID']
        Spell_Level = request.POST['Spell_Level']
        School_ID = request.POST['School']
        Time_Application = request.POST['Time_Application']
        Distance = request.POST['Distance']
        Duration = request.POST['Duration']
        Components = request.POST['Components']
        Archetypes_ID = request.POST['Archetypes']
        Description = request.POST['Description']

        try:
            school_id = School.objects.get(pk=School_ID)
            archetypes_id = Archetypes.objects.get(pk=Archetypes_ID)

            if Spell_ID and Spell_Level and school_id and Components and archetypes_id:
                Spells.objects.create(Spell_ID = Spell_ID,
                                      Spell_Author_id=request.user.pk,
                                      Spell_Level = Spell_Level,
                                      School = school_id,
                                      Time_Application = Time_Application,
                                      Distance = Distance,
                                      Duration = Duration,
                                      Components = Components,
                                      Archetypes = archetypes_id,
                                      Description = Description, )
                status = 'Ok'
        except:
            status = 'Error'
    else:
        form = SpellCreateForm()

    schools = School.objects.all()
    archetypes = Archetypes.objects.all()

    context = {'form': form,
               'schools': schools,
               'archetypes': archetypes,
               'status': status, }

    return render(request, 'home/spells_create.html', context)


@login_required(login_url='home:login')
def spells_delete(request):
    if request.method == 'POST':
        form = SpellFindForm(data=request.POST)
        Spell_ID = request.POST['Spell_ID']
        Spell_Level = request.POST['Spell_Level']
        School_ID = request.POST['School']
        Archetypes_ID = request.POST['Archetypes']

        filter_params = {}

        if Spell_ID:
            filter_params['Spell_ID'] = Spell_ID

        if Spell_Level:
            filter_params['Spell_Level'] = Spell_Level

        if School_ID:
            filter_params['School'] = School_ID

        if Archetypes_ID:
            filter_params['Archetypes'] = Archetypes_ID

        filter_params['Spell_Author_id'] = request.user.pk

        if len(filter_params)>1:
            try:
                Spells.objects.filter(**filter_params).delete()
                status = 'Ok'
            except:
                status = 'Error'
        else:
            status = 'Nothing'

    else:
        form = SpellDeleteForm()
        status = 'Nothing'

    schools = School.objects.all()
    archetypes = Archetypes.objects.all()

    context = {'form': form,
               'schools': schools,
               'archetypes': archetypes,
               'status': status, }

    return render(request, 'home/spells_delete.html', context)