from django.urls import path
from .views import *



urlpatterns = [
    path('', login_system,name='login'),
    path('register',register_user,name='register'),
    path('home',to_home_page,name='home'),
    path('logout', logout_system, name='logout'),
    path('delete/<int:id>', delete, name='delete'),
    path('update',update_user, name='update'),
]