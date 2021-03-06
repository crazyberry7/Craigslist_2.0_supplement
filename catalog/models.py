from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from localflavor.us.models import USZipCodeField, USStateField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.geos import Point
#from users.models import CustomUser
# Create your models here.


class Posting(models.Model):

    CONDITIONS = (
	('N', 'New'),
	('LN', 'New, Open-Box'),
	('R', 'Refurbished'),
        ('U', 'Used'),
	('FP', 'For Parts or not working'),
              	    )
    #sample_user = CustomUser.objects.create_custom_user('Brian', 'Wang', 'ipadproman14@gmail.com', 'abcdef', False, 'ipadproman14', False, True, '2011-01-01')
    
    #sample_user = User.objects.create_user('john', 'john@gmail.com', 'password') 
    #Fields
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=2, related_name='+')
    number_id = models.IntegerField(default=None, null=True, blank=True)
    username = models.CharField(max_length = 30, default=None, null=True, blank=True) 
    title = models.CharField(max_length = 50, default=None, null=True)
    post_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    description = models.TextField(default=None, null=True, blank=True)
    price = models.IntegerField(default=None, null=True)
    condition = models.CharField(max_length = 20, choices = CONDITIONS, null=True)
    email = models.EmailField(default=None, null=True)
    contact_name = models.CharField(max_length = 30, null=True, blank=True)
    url = models.CharField(max_length = 30, null=True, blank=True)
    street = models.CharField(max_length = 30, null=True, blank=True)
    city = models.CharField(max_length = 30, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zipcode = USZipCodeField(null=True)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    text = models.BooleanField(default=False)
    call = models.BooleanField(default=False)
    phone_number = PhoneNumberField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    
    readonly_fields=('user',) 
    class Meta:
        ordering = ["-post_date"]
    """
    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])
    """
    def __str__(self):
        return self.title

    def get_location(self):
        return Point(self.longitude, self.latitude)
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return settings.MEDIA_ROOT + "/%s-%s" % (slug, filename)  


class Images(models.Model):
    post = models.ForeignKey(Posting, null=True, blank=True, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)

"""
class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')
    posting = models.ForeignKey(Posting, null=True, blank=True, verbose_name='posting', on_delete=models.CASCADE)
"""
