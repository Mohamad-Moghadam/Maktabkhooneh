from django.db import models

class Programming_Courses(models.Model):
    name = models.CharField(max_length = 100)
    #teacher = models.ForeignKey(to = Teachers, on_delete=models.CASCADE)
    price = models.IntegerField()
    number_of_students = models.IntegerField()
    sessions = models.IntegerField()
    rating = models.IntegerField()
    hours = models.IntegerField()

