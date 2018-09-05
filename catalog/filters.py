import django_filters
from .models import Posting

class PostingFilter(django_filters.FilterSet):
 	class Meta:
            model = Posting
            fields =  {
		'price': ['lt', 'gt'],
                'zipcode': ['exact'],
	    }
