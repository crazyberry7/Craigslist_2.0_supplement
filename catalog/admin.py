from django.contrib import admin
from .models import Posting
# Register your models here.

#admin.site.register(Posting)

class PostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'condition', 'price')

admin.site.register(Posting, PostingAdmin)
