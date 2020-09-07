from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. ar card index")
    #return render(request, 'index.html', {})
