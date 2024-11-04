from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return HttpResponse("INDEX 4")

def update(request):
    os.system("git pull origin main")
    return HttpResponse("UPDATE")