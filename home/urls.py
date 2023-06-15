from django.urls import path
from home.views import bestiary_find, bestiary_create, bestiary_delete, items_find, items_create, items_delete, spells_find, spells_create, spells_delete, index, login, registration


app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('bestiary/find/', bestiary_find, name='bestiary_find'),
    path('bestiary/create/', bestiary_create, name='bestiary_create'),
    path('bestiary/delete/', bestiary_delete, name='bestiary_delete'),
    path('items/find/', items_find, name='items_find'),
    path('items/create/', items_create, name='items_create'),
    path('items/delete/', items_delete, name='items_delete'),
    path('spells/find/', spells_find, name='spells_find'),
    path('spells/create/', spells_create, name='spells_create'),
    path('spells/delete/', spells_delete, name='spells_delete'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
]