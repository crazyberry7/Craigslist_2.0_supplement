from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views 
from catalog.forms import Posting_Form_Final, Posting_Form_Final, Posting_Form_Title, Posting_Form_Description, Posting_Form_Contact, Posting_Form_Location
from catalog.views import OrderWizard
from users.views import my_profile




urlpatterns = [
    #path('', views.index, name='index'),
    path('item/detail/<int:id>', views.post_detail, name='post_detail'),
    #path('post/create', views.post_create)
    path('item/create', login_required(OrderWizard.as_view([Posting_Form_Title, Posting_Form_Description, Posting_Form_Contact, Posting_Form_Location])), name='create'),
    path('accounts/profile', my_profile, name='my_profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

