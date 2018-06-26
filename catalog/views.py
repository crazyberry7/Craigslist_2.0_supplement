from django.shortcuts import render, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView
from .forms import Query
import os 

from .models import Posting
from .forms import Posting_Form_Title, Posting_Form_Contact, Posting_Form_Description, Posting_Form_Location, Posting_Form_Final

# Create your views here.
#View interacts with database to retrieve data
#that can be displayed through template (html)
"""
def index(request):
    return render(request, 'index.html')
"""
#Don't need a views for interacting with database for search results b/c Elasticsearch has a built-int
#feature that updates it's on search models with Django database. Just follow haystack instructions
# and add url mapping and search.html page and i'm good to go

"""
FORMS = [("Title", Posting_Form_Title),
	 ("Contact", Posting_Form_Contact),
	 ("Description", Posting_Form_Description),
	 ("Location", Posting_Form_Location)]
"""
class OrderWizard(SessionWizardView):
        template_name = "contact_form.html"
        file_storage = FileSystemStorage(location= os.path.join(settings.MEDIA_ROOT, 'photos'))
        #def get_template_names(self):
        #    return [TEMPLATES[self.steps.current]]

        def done(self, form_list, form_dict, **kwargs): 
            form_data = process_form_data(form_list)
            return render_to_response('done.html', {'form_data': form_data})

def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    form = Posting_Form_Final()
    instance = form.save(commit=False)
    instance.title = form_data[0]['title']
    instance.image = form_data[0]['image']
    instance.condition = form_data[1]['condition']
    instance.description = form_data[1]['description']
    instance.price = form_data[2]['price']
    instance.email = form_data[2]['email']
    instance.phone_number = form_data[2]['phone_number']
    instance.street = form_data[3]['street']
    instance.city = form_data[3]['city']
    instance.state = form_data[3]['state']
    instance.zip_code = form_data[3]['zipcode']
    instance.save()
    return form_list

def post_detail(request, id=None):
   instance = get_object_or_404(Posting, id=id)
   context = {
	'title': instance.title,
	'instance': instance,
    }
   return render(request, 'post_detail.html', context) 

@login_required
def post_create(request):
    form = Posting_Form_Title(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.number_id = request.user.id
        instance.username = request.user.username
        instance.save()
    else:
        form = Posting_Form_Title()
    context = {
	    'form': form,
    }
    return render(request, 'post_form.html', context)



