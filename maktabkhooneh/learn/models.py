from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length = 100)
    teacher = models.ManyToManyField('learn.Teacher', verbose_name = ("teachers"))
    price = models.IntegerField()
    number_of_students = models.IntegerField()
    sessions = models.IntegerField()
    rating = models.IntegerField()
    hours = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    discription = models.TextField()
    number_of_students = models.IntegerField()

