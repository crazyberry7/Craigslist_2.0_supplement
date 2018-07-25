from django.urls import path
from django.config.urls import url
from django.contrib.auth import views as auth_views
from .views import my_profile

#import users.views

#app_name = 'users'

urlpatterns = [
    #url(r'^login/', auth_views.login, {'next_page': 'homepage'}),
    #url(r'^logout/', auth_views.logout,  name='logout'),
    #path('login', LoginView.as_view(), name='login2'),
    #path('logout', LogoutView.as_view(), name='logout2'),
]
