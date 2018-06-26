from django.urls import path
from . import views
from catalog.forms import Posting_Form_Final, Posting_Form_Final, Posting_Form_Title, Posting_Form_Description, Posting_Form_Contact, Posting_Form_Location
from catalog.views import OrderWizard





urlpatterns = [
    #path('', views.index, name='index'),
    path('post/<int:id>', views.post_detail, name='post_detail'),
    #path('post/create', views.post_create)
    path('create', OrderWizard.as_view([Posting_Form_Title, Posting_Form_Description, Posting_Form_Contact, Posting_Form_Location])),


]
