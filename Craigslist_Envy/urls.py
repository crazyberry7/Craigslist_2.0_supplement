from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from django.views.generic import TemplateView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registration import views as views
from catalog.views import CatalogSearchView
from catalog.views import homepage
from catalog.views import SearchView


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [

    path('catalog/', include('catalog.urls')),

    #path('search/', include('haystack.urls'), name= 'blah'),
    #path('search/', CatalogSearchView.as_view()),
    path('search/', SearchView(), name='temp_homepage'),
    #path('', include('haystack.urls'), name='homepage'),
    path('', homepage, name='homepage'),

    path('users/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup_view'),
    path('users/logout/', views.logout, name='logout_view'),
    path('users/login/', login, {'next_page': '/'}),

    #path('accounts/', include('allauth.urls')),
    path('about/', TemplateView.as_view(template_name="about.html")), 

    #images upload 
    path('images', TemplateView.as_view(template_name='base.html'), name='home'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







