from django.db import models
#from courses.models import Course
#from address.models import Addres

class Dossier(models.Model):

    FEVORIT_COLOR = (
            ('red', 'red'),
            ('orange', 'orange'),
            ('yellow', 'yellow'),
            ('green', 'green'),
            ('blue', 'blue'),
            ('pink', 'pink'),
            ('violet', 'violet'),
        )
    address = models.ForeignKey('address.Addres')
    courses = models.ManyToManyField('courses.Course')
    color = models.CharField(max_length=15, choices=FEVORIT_COLOR)
    def __unicode__(self):
         return self.color 

