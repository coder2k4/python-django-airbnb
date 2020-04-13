from django.shortcuts import render

# Create your views here.
from rooms.models import Room


def home(request):
    return render(request, 'base.html')
