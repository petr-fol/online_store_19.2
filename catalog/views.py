from django.shortcuts import render
import os

# home = os.path.


def home(request):
    return render(request, 'catalog/home.html')
# templates/


def catalog(request):
    return render(request, 'catalog/contact.html')
