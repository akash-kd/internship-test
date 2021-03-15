
from django.urls import path
from .views import regis,login

urlpatterns = [
    path('login/',login,name='profile-login'),
    path('regis/',regis,name='profile-regis')
]