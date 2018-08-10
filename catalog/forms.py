from django import forms
from .models import Posting
from .models import Images
from multiupload.fields import MultiFileField, MultiMediaField

"""
class UploadImagesForm(forms.Form):
     attachments = MultiMediaField(
        min_num=0, 
        max_num=10, 
        max_file_size=1024*1024*5, 
        media_type='image'  # 'audio', 'video' or 'image'
    )
"""

class Query(forms.Form):
   query = forms.CharField(max_length=100)

   def get_query(self):
        return query

class Zipcode_Form(forms.ModelForm):
        class Meta:
            model = Posting
            fields = ('zipcode',)

class Posting_Form_Final(forms.ModelForm):
        class Meta:
            model = Posting
            fields = ('user','title', 'image', 'condition', 'description',
			'price', 'email', 'phone_number', 'street', 'city', 'state',
			'zipcode',)

class ImagesForm(forms.ModelForm):
        class Meta:
             model = Images
             fields = ('image', 'post', )

class Posting_Form_Title(forms.ModelForm):
	class Meta:
	    model = Posting
	    fields = ('title', 'image')
	#attachments = MultiMediaField(min_num=0, max_num=10,max_file_size=1024*1024*5, media_type='image')
        
	"""
        def save(self, commit=True):
            instance = super(Posting_Form_Title, self).save(commit)
            for each in self.cleaned_data['files']:
                Attachment.objects.create(file=each, message=instance)
            return instance 
	"""
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




