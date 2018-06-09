from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
#from users.models import CustomUser
# Create your models here.



class Posting(models.Model):

    CONDITIONS = (
        ('U', 'Used'),
        ('N', 'New'),
        ('LN', 'New, Open-Box'),
    )
    #sample_user = CustomUser.objects.create_custom_user('Brian', 'Wang', 'ipadproman14@gmail.com', 'abcdef', False, 'ipadproman14', False, True, '2011-01-01')
    
    #sample_user = User.objects.create_user('john', 'john@gmail.com', 'password') 
    #Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='+')
    title = models.CharField(max_length = 50, default=None, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    description = models.TextField(default=None, null=True, blank=True)
    price = models.IntegerField(default=None, null=True, blank=True)
    condition = models.CharField(max_length = 20, choices = CONDITIONS, null=True, blank=True)
    email = models.CharField(max_length = 30, default=None, null=True, blank=True)
    contact_name = models.CharField(max_length = 30, null=True, blank=True)
    
    class Meta:
        ordering = ["update_date"]
    """
    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])
    """
    def __str__(self):
        return self.title


