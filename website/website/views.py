from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> hello shashwat </h1>")