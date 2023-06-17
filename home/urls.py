from django.urls import path

from home.views import login, registration, logout_view, index
from home.views import bestiary_find, bestiary_create
from home.views import bestiary_delete, spells_create, spells_delete
from home.views import items_find, items_create, items_delete
from home.views import spells_find, spell_detail, item_detail, bestiary_detail

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('bestiary/find/', bestiary_find, name='bestiary_find'),
    path('bestiary/create/', bestiary_create, name='bestiary_create'),
    path('bestiary/delete/', bestiary_delete, name='bestiary_delete'),
    path('items/find/', items_find, name='items_find'),
    path('items/create/', items_create, name='items_create'),
    path('items/delete/', items_delete, name='items_delete'),
    path('spells/find/', spells_find, name='spells_find'),
    path('spells/create/', spells_create, name='spells_create'),
    path('spells/delete/', spells_delete, name='spells_delete'),
    path('spells/<int:spell_id>', spell_detail, name='spell_detail'),
    path('items/<int:item_id>', item_detail, name='item_detail'),
    path('bestiary/<int:bestiary_id>', bestiary_detail, name='bestiary_detail'),
]