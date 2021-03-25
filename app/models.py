from django.db import models


class Course(models.Model):
    #we will have an auto increment field in Django that is 'id',but we can initialise as well
    crs_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Student(models.Model):
    st_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
