from django.db import models

# Create your models here.



class Posting(models.Model):

    CONDITIONS = (
        ('U', 'Used'),
        ('N', 'New'),
        ('LN', 'New, Open-Box'),
    )
    
    #Fields
    title = models.CharField(max_length = 50)
    post_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    description = models.TextField()
    price = models.IntegerField()
    condition = models.CharField(max_length = 20, choices = CONDITIONS)
    
    class Meta:
        ordering = ["update_date"]
    """
    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])
    """
    def __str__(self):
        return self.title

