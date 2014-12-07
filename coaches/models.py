from django.db import models

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