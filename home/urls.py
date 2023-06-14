from django.urls import path
from home.views import index, home, download


app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('generate/', home, name='home'),
    path('download/<path:path>', download, name='download')
]