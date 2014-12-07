from django.db import models

class Student(models.Model):

    PACKAGE_LIST = (
        ('Gold', 'Gold'),
        ('Standart', 'Standart'),
        ('VIP', 'VIP'),
    )

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=10, choices=PACKAGE_LIST)


# Create your models here.
