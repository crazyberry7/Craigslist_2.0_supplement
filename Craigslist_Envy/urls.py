"""Craigslist_Envy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registration import views as views
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [

    path('catalog/', include('catalog.urls')),

    path('search/', include('haystack.urls'), name= 'blah'),
    path('', include('haystack.urls'), name='homepage'),

    path('users/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup_view'),
    path('users/logout/', views.logout, name='logout_view'),
    path('users/login/', login, {'next_page': '/'}),

    #path('accounts/', include('allauth.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)








