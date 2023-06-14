from django.contrib import admin
from django.urls import path, include
from home.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bestiary/', include('home.urls', namespace='bestiary_find')),
    path('bestiary/', include('home.urls', namespace='bestiary_create')),
    path('bestiary/', include('home.urls', namespace='bestiary_delete')),
    path('items/', include('home.urls', namespace='items_find')),
    path('items/', include('home.urls', namespace='items_create')),
    path('items/', include('home.urls', namespace='items_delete')),
    path('spells/', include('home.urls', namespace='spells_find')),
    path('spells/', include('home.urls', namespace='spells_create')),
    path('spells/', include('home.urls', namespace='spells_delete')),
]
