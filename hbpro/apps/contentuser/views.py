from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'contentuser/index.html')
    #return HttpResponse("Index")


def imdexTeam(request):
    return render(request, 'contentuser/imdex.html')