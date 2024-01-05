# models.py
from django.db import models

class Course(models.Model):
    percentage = models.IntegerField()
    parent_course = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

