from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("INDEX 2")

def update(request):
    return HttpResponse("UPDATE")