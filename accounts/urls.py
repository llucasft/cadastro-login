from . import views
from django.urls import path 


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logoutaccount/', views.logoutaccount, name='logoutaccount'),
]