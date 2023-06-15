from django.contrib import admin
from django.urls import path, include
from home.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('home.urls', namespace='bestiary_find')),
    path('', include('home.urls', namespace='bestiary_create')),
    path('', include('home.urls', namespace='bestiary_delete')),
    path('', include('home.urls', namespace='items_find')),
    path('', include('home.urls', namespace='items_create')),
    path('', include('home.urls', namespace='items_delete')),
    path('', include('home.urls', namespace='spells_find')),
    path('', include('home.urls', namespace='spells_create')),
    path('', include('home.urls', namespace='spells_delete')),
]
