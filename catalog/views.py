from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Query
# Create your views here.

#View interacts with database to retrieve data
#that can be displayed through template (html)
def index(request):
    return render(request, 'index.html')

"""
def render_search(request):
    if request.method == 'GET':
        form = Query(request.GET) 
        search_words = form.cleaned_data['query']
        return render(request, 'catalog/search_results.html', {'search_words': search_words})
    else:
        form = Query()
"""
#Don't need a views for interacting with database for search results b/c Elasticsearch has a built-int
#feature that updates it's on search models with Django database. Just follow haystack instructions
# and add url mapping and search.html page and i'm good to go
