from django.urls import path
from landings.views import landings, selected_roadmap

urlpatterns = [
    path('', landings),
    path('roadmaps/<str:topic>', selected_roadmap),

]
