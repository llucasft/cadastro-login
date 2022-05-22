from . import views
from django.urls import path 


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('logoutaccount/', views.logoutaccount, name='logoutaccount'),
]