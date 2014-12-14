from django.db import models
from django.contrib.auth.models import User
#from dossier.models import Dossier

class Coach(models.Model):

    JOB_LIST = (
        ('teacher', 'teacher'),
        ('assistant', 'assistant'),
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    name_cours = models.CharField(max_length=50)
    job_title = models.CharField(max_length=10, choices=JOB_LIST)
    job_status = models.ForeignKey(User)
    dossier = models.OneToOneField('dossier.Dossier', related_name='Dossier_of')

    def __unicode__(self):
         visual_list = self.name + ' ' + self.surname
         return visual_list
