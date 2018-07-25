from django.utils import timezone
from haystack import indexes
from catalog.models import Posting



class PostingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    update_date = indexes.DateTimeField(model_attr='update_date') 
    location = indexes.LocationField(model_attr='get_location')


    def get_model(self):
        return Posting


    def index_queryset(self, using=None):
        return self.get_model().objects.filter(update_date__lte=timezone.now())
