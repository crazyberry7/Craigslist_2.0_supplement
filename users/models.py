from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

"""
class CustomUserManager(models.Manager):
    def create_custom_user(self, first_name, last_name, email, password,is_superuser, username, is_staff, is_active, date_joined):
        user = self.create(first_name=first_name, last_name=last_name, email=email, password=password,is_superuser=is_superuser, username=username, is_staff=is_staff, is_active=is_active, date_joined=date_joined)
        return user

"""
"""
#By default, abstract users have first, last name and email attributes
class CustomUser(models.Model):
    #Each user can have many postings
    #postings = models.ForeignKey(Posting, related_name='postings')
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    objects = CustomUserManager()
    is_superuser = models.BooleanField()
    username =  models.CharField(max_length = 50, unique=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateField()
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    #Specifies email rather than username as the identifier of a user 
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name',)
    def __str__(self):
        return self.first_name + self.last_name
"""
class customuser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_general_member = models.BooleanField(default=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    username = models.CharField(max_length = 30)
	
    def __str__(self):
      	return self.username
