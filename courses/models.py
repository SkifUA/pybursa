from django.db import models
#from coaches.models import Coach

class Course(models.Model):

    COURS_LIST = (
        ('python', 'python'),
        ('JS', 'JS'), 
        ('rubybursa', 'rubybursa')
    )

    tehnology = models.CharField(max_length=10, choices=COURS_LIST, blank=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField()
    description = models.CharField(max_length=250, blank=True, null=True)
    teacher = models.CharField(max_length=150, blank=True, null=True)
    assistent = models.CharField(max_length=150, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField()


    def __unicode__(self):
         return self.name 
    