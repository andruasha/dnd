from django.contrib import admin
from django.urls import path, include
from home.views import index
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
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
    path('', include('home.urls', namespace='login')),
    path('', include('home.urls', namespace='registration')),
]
