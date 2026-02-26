from django.urls import path

from .views import *


urlpatterns = [
        path('', home, name='home'),
        path('home/', home, name='home'),
        path('register/', register, name='register'),
        path('login/', login_view, name='login'),
        path('packages/', packages, name='packages'),
        path('logout/', logout_view, name='logout'),
        
]