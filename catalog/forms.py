from django import forms
from .models import Posting

class Query(forms.Form):
   query = forms.CharField(max_length=100)

   def get_query(self):
        return query


class Posting_Form(forms.ModelForm):
	class Meta:
	    model = Posting
	    fields = ('title', 'condition','description', 'price', 'email',)


