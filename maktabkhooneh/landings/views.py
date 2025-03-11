from django.http.response import HttpResponse

def landings(request):
    return HttpResponse("Hi ,Choose your roadmap.")

def selected_roadmap(request, topic):
    return HttpResponse("This page is the roadmap for you to learn {topic}.")
