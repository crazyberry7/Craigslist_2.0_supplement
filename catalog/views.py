from django.shortcuts import render, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import SuspiciousOperation
from formtools.wizard.views import SessionWizardView
from .forms import Query
from .forms import Zipcode_Form
from .filters import PostingFilter
import os 
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet
from haystack.forms import ModelSearchForm
from haystack.utils.geo import Point, D
from .models import Posting
from .forms import Posting_Form_Title, Posting_Form_Contact, Posting_Form_Description, Posting_Form_Location, Posting_Form_Final
from django.contrib.gis.geoip2 import GeoIP2
from uszipcode import ZipcodeSearchEngine
import zipcode
# Create your views here.
#View interacts with database to retrieve data
#that can be displayed through template (html)


#imported from haystack/views.py


from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from django.shortcuts import render

from haystack.forms import FacetedSearchForm, ModelSearchForm
from haystack.query import EmptySearchQuerySet

RESULTS_PER_PAGE = getattr(settings, "HAYSTACK_SEARCH_RESULTS_PER_PAGE", 20)

"""
def index(request):
    return render(request, 'index.html')
"""
#Don't need a views for interacting with database for search results b/c Elasticsearch has a built-int
#feature that updates it's on search models with Django database. Just follow haystack instructions
# and add url mapping and search.html page and i'm good to go



class SearchView(object):
    template = "search/search.html"
    extra_context = {}
    query = ""
    results = EmptySearchQuerySet()
    request = None
    form = None
    results_per_page = RESULTS_PER_PAGE

    def __init__(
        self,
        template=None,
        load_all=True,
        form_class=None,
        searchqueryset= None,
        results_per_page=None,
	zipcode_provided = False,
	sqs=None,
        zipcode_form=None,
        zipcode=None,
    ):
        self.load_all = load_all
        self.form_class = form_class
        self.searchqueryset = SearchQuerySet().order_by('-update_date')
        #self.searchqueryset = None
        self.zipcode_provided = zipcode_provided
        self.sqs = sqs	
        self.zipcode_form = zipcode_form
        self.zipcode= zipcode
        self.city = None
        self.state = None


        if form_class is None:
            self.form_class = ModelSearchForm

        if not results_per_page is None:
            self.results_per_page = results_per_page

        if template:
            self.template = template
    
    def __call__(self, request):
        """
        Generates the actual response to the search.
        Relies on internal, overridable methods to construct the response.
        """
        self.request = request
	
        if self.is_zipcode_provided(self.request):
            self.zipcode_provided = True

        self.form = self.build_form()
        self.query = self.get_query()
        self.results = self.get_results()
        #import pdb; pdb.set_trace()
        return self.create_response()
    def is_zipcode_provided(self, request):
        #self.zipcode = self.request.GET.get('zipcode')
        if request.GET.get('zipcode'):
            return True
        else:
            return False

    def build_form(self, form_kwargs=None):
        """
        Instantiates the form the class should use to process the search query.
        """
        data = None
        kwargs = {"load_all": self.load_all}
        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.GET):
            data = self.request.GET
	# Radius is defaulted to 30 miles	
        #import pdb; pdb.set_trace()
        if self.request.GET.get('zipcode'):
            self.zipcode = self.request.GET.get('zipcode')
            """
            search = ZipcodeSearchEngine()
            zip = search.by_zipcode(zip_code) 
            longitude = zip['Longitude']
            lat = zip['Latitude']
            """
            zip = zipcode.isequal(str(self.zipcode))
            longitude = zip.lng
            lat = zip.lat
            self.city = zip.city
            self.state = zip.state
            self.searchqueryset = SearchQuerySet().dwithin('location', Point(longitude, lat), D(mi=30))
            #f = PostingFilter(self.request.GET, queryset=sqs)
        else:
            ip = '24.6.173.143'
            g = GeoIP2()
            location_dict = g.city(ip) 
            self.city = location_dict['city']
            self.state = location_dict['region']
            lat = location_dict['latitude']
            longitude = location_dict['longitude']
            self.zipcode = location_dict['postal_code']
            self.searchqueryset = SearchQuerySet().dwithin('location', Point(longitude, lat), D(mi=30))
            #f = PostingFilter(self.request.GET, queryset=sqs)
        if self.searchqueryset is not None:
            kwargs["searchqueryset"] = self.searchqueryset
        
        self.zipcode_form = Zipcode_Form(self.request.GET)
        
        return self.form_class(data, **kwargs)

    def get_query(self):
        """
        Returns the query provided by the user.
        Returns an empty string if the query is invalid.
        """
        if self.form.is_valid():
            return self.form.cleaned_data["q"]

        return ""

    def get_results(self):
        """
        Fetches the results via the form.
        Returns an empty list if there's no query to search with.
        """
        #import ipdb; ipdb.set_trace()

        return self.form.search()

    def build_page(self):
        """
        Paginates the results appropriately.
        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.GET.get("page", 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results[start_offset : start_offset + self.results_per_page]

        paginator = Paginator(self.results, self.results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)

    def extra_context(self):
        """
        Allows the addition of more context variables as needed.
        Must return a dictionary.
        """
        return {}

    def get_context(self):
        (paginator, page) = self.build_page()

        context = {
            "query": self.query,
            "zipcode_provided": self.zipcode_provided,
            "zipcode_form": self.zipcode_form,
            "sqs": self.sqs,
            "form": self.form,
            "page": page,
            "paginator": paginator,
            "suggestion": None,
            "zipcode": self.zipcode,
	    "city" : self.city,
	    "state": self.state,
        }

        if (
            hasattr(self.results, "query")
            and self.results.query.backend.include_spelling
        ):
            context["suggestion"] = self.form.get_suggestion()

        context.update(self.extra_context())

        return context

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """

        context = self.get_context()

        return render(self.request, self.template, context)



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
    instance.zipcode = form_data[3]['zipcode']
    instance.height_field = 100 
    instance.width_field = 100
    search = ZipcodeSearchEngine()
    zipcode = search.by_zipcode(instance.zipcode)
    instance.longitude = zipcode['Longitude']
    instance.latitude = zipcode['Latitude']
    instance.save()
    return form_list

def homepage(request):
    ip_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_forwarded:
        ip = ip_forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #convert ip into zipcode
    #if user doesn't input zipcode/location, default will be the automatically
    #converted zipcode
    if request.GET.get('zipcode'):
        query = request.GET.get('q')
        zip_code = request.GET.get('zipcode')
        """ 
        search = ZipcodeSearchEngine()
        zip = search.by_zipcode(zip_code) 
        longitude = zip['Longitude']
        lat = zip['Latitude']
        """
        zip = zipcode.isequal(str(zip_code))
        longitude = 0.00
        lat = 0.00
        sqs = SearchQuerySet().dwithin('location', Point(longitude, lat), D(mi=30))
        f = PostingFilter(request.GET, queryset=sqs)

        context = {
 	'city': zip['City'],
	'filter': f,
   	'sqs': sqs,
        'zipcode':'00001',
   	'query': query,
        }

    else:
        #Temporary stand-in ip-address
        query = request.GET.get('q')
        ip = '24.6.173.143'
        g = GeoIP2()
        location_dict = g.city(ip) 
        city = location_dict['city']
        lat = location_dict['latitude']
        longitude = location_dict['longitude']
        zip_code = location_dict['postal_code']
        #sqs = SearchQuerySet()
        sqs = SearchQuerySet().dwithin('location', Point(longitude, lat), D(mi=30))
        f = PostingFilter(request.GET, queryset=sqs)
        context = {
 	'city': city,
	'filter': f,
   	'sqs': sqs,
        'zipcode': '10001',
  	'query': query,
        }
    return render(request, 'search/filter_template.html', context)
def post_detail(request, id=None):
   instance = get_object_or_404(Posting, id=id)
   context = {
	'title': instance.title,
	'instance': instance,
    }
   return render(request, 'post_detail.html', context) 

class CatalogSearchView(SearchView):
    template_name = 'search/search.html'
    queryset = SearchQuerySet().order_by('-update_date')
    form_class = ModelSearchForm

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



