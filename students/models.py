from django.db import models
#from dossier.models import Dossier

class Student(models.Model):

    PACKAGE_LIST = (
        ('Gold', 'Gold'),
        ('Standart', 'Standart'),
        ('VIP', 'VIP'),
    )

    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField()
    surname = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    package = models.CharField(max_length=10, choices=PACKAGE_LIST)
    #note = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField('courses.Course')
    dossier = models.ForeignKey('dossier.Dossier') 

    def __unicode__(self):
         visual_list = self.name + ' ' + self.surname
         return visual_list


# Create your models here.
