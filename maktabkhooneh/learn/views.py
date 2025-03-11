from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from learn.models import Programming_Courses

def courses(request, course_type: str):
    HttpResponse(f"{course_type}")

