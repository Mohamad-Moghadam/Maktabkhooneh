from django.urls import path
from learn.views import courses

urlpatterns = [
    path('<str:course_type>', courses)
]
