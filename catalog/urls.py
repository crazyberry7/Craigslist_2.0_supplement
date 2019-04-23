from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from . import views 
from catalog.forms import Posting_Form_Final, Posting_Form_Title, Posting_Form_Description, Posting_Form_Contact, Posting_Form_Location
from catalog.views import OrderWizard
from users.views import my_profile


FORMS = [("Title", Posting_Form_Title),
	 ("Contact", Posting_Form_Contact),
	 ("Description", Posting_Form_Description),
	 ("Location", Posting_Form_Location)]


urlpatterns = [
    #path('', views.index, name='index'),
    path('item/detail/<int:id>', views.post_detail, name='post_detail'),
    #path('post/create', views.post_create)
    path('item/create', login_required(OrderWizard.as_view([Posting_Form_Title, Posting_Form_Description, Posting_Form_Contact, Posting_Form_Location])), name='create'),
    #path('item/create', login_required(OrderWizard.as_view(FORMS)), name='create'),
    path('accounts/settings', my_profile, name='my_settings'),
    path('basic_images_upload', views.ImagesUploadView.as_view(), name='basic_images_upload'),
    path('progress-bar-upload', login_required(views.ProgressBarUploadView.as_view()), name='progress_bar_upload'),
    path('drag-and-drop-upload', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
    path('clear', views.clear_database, name='clear_database'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

