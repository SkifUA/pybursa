from django.db import models

class Addres(models.Model):

    post_index = models.IntegerField(max_length=8, blank=True, null=True)
    country = models.CharField(max_length=70, blank=False)
    region = models.CharField(max_length=80, blank=False)
    area = models.CharField(max_length=80, blank=True, null=True)
    street = models.CharField(max_length=100, blank=False)
    build = models.CharField(max_length=8, blank=False)

    def __unicode__(self):
         return self.region 
    

    
# Create your models here.
