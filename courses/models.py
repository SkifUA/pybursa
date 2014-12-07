from django.db import models

class Course(models.Model):

    COURS_LIST = (
        ('python', 'python'),
        ('JS', 'JS'),
    )

    tehnology = models.CharField(max_length=10, choices=COURS_LIST)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    teacher = models.CharField(max_length=150)
    assistent = models.CharField(max_length=150)
    date_start = models.DateField()
    date_end = models.DateField()
    