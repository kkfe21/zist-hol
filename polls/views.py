from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Your'are at the polls index.")
