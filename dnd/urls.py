from django.contrib import admin
from django.urls import path, include
from home.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', include('home.urls', namespace='home')),
    path('users/', include('users.urls', namespace='users')),
]
