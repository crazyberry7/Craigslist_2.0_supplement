from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView
from .forms import Query

from .models import Posting
from .forms import Posting_Form_Title, Posting_Form_Contact, Posting_Form_Description, Posting_Form_Location

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

FORMS = [("Title", Posting_Form_Title),
	 ("Contact", Posting_Form_Contact),
	 ("Description", Posting_Form_Description),
	 ("Location", Posting_Form_Location)]

class OrderWizard(SessionWizardView):
	def get_template_names(self):
            return [TEMPLATES[self.steps.current]]

	def done(self, form_list, form_dict, **kwargs): 
            form  


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
        form = Posting_Form()
    context = {
	    'form': form,
    }
    return render(request, 'post_form.html', context)



