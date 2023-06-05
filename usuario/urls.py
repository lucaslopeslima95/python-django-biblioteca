from django.urls import path
from .views import *

urlpatterns = [
    path('', login_sistem,name='login'),
    path('register',register,name='register'),
    path('home',home,name='home'),
    path('logout', logout_sis, name='logout'),
]