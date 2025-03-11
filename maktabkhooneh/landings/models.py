from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    discription = models.TextField()
    number_of_students = models.IntegerField()

class Courses(models.Model):
    name = models.CharField(max_length = 100)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, related_name="teacher_course")
    price = models.IntegerField()
    number_of_students = models.IntegerField()
    sessions = models.IntegerField()
    rating = models.IntegerField()
    hours = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length = 100)
    maktabplus_sub = models.BooleanField(default = False)
    courses = models.ForeignKey(to = Courses, on_delete = models.CASCADE, related_name = "courses_of_the_students")
    certifications = models.TextField()
    asked_questions = models.TextField()
    payments = models.TextField()
    cart = models.ForeignKey(to = Courses, on_delete = models.CASCADE, related_name = "purchased_courses")

class purchased(models.Model):
    courses = models.ForeignKey(to = Courses, on_delete = models.CASCADE, related_name = "purchaced_courses")
    student = models.ForeignKey(to = Student, on_delete= models.CASCADE, related_name="student_purchases")
    

