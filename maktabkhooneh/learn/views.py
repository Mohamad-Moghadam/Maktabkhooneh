from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from learn.models import Programming_Courses

def courses(request, course_type: str):
    return HttpResponse(f"{course_type}")

