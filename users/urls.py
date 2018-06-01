from django.urls import path
from django.confg.urls import url
from django.contrib.auth import views as auth_views


#import users.views

#app_name = 'users'

urlpatterns = [
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout,  name='logout'),
    #path('login', LoginView.as_view(), name='login2'),
    #path('logout', LogoutView.as_view(), name='logout2'),


]
