# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Abuse(models.Model):

    
    name = models.ForeignKey('coaches.Coach', verbose_name=_("To whom"))
    
    surname = models.ForeignKey('students.Student', verbose_name=_("Of whom"))
    courses = models.ForeignKey('courses.Course', verbose_name=_("Course"))
    #name_student = models.CharField(max_length=50, blank=False)
    email = models.EmailField(null=True)
    text = models.CharField(_("What made"), max_length=255, blank=True, null=True)

    def __unicode__(self):
         
         return self.pk


