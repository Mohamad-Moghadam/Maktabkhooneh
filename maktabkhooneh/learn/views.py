from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from learn.models import Programming_Courses

def courses(request, course_type: str):
    if course_type == 'programming':
        JsonResponse(Programming_Courses)

