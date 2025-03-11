from django.urls import path
from landings.views import landings, selected_roadmap

urlpatterns = [
    path('', landings),
    path('roadmaps', selected_roadmap),
    
]
