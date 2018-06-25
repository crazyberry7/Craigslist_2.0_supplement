from django import forms
from .models import Posting

class Query(forms.Form):
   query = forms.CharField(max_length=100)

   def get_query(self):
        return query


class Posting_Form_Title(forms.ModelForm):
	class Meta:
	    model = Posting
	    fields = ('title', 'image',)

class Posting_Form_Description(forms.ModelForm):
	class Meta:
	    model = Posting
	    fields = ('condition', 'description',)

class Posting_Form_Contact(forms.ModelForm):
	class Meta:
	    model = Posting
	    fields = ('price', 'email', 'phone_number',)

class Posting_Form_Location(forms.ModelForm):
	class Meta:
	    model = Posting
	    fields = ('street', 'city', 'state', 'zipcode',)




