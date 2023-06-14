from django.urls import path
from home.views import bestiary_find, bestiary_create, bestiary_delete, items_find, items_create, items_delete, spells_find, spells_create, spells_delete, index


app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('find/', bestiary_find, name='bestiary_find'),
    path('create/', bestiary_create, name='bestiary_create'),
    path('delete/', bestiary_delete, name='bestiary_delete'),
    path('find/', items_find, name='items_find'),
    path('create/', items_create, name='items_create'),
    path('delete/', items_delete, name='items_delete'),
    path('find/', spells_find, name='spells_find'),
    path('create/', spells_create, name='spells_create'),
    path('delete/', spells_delete, name='spells_delete'),
]