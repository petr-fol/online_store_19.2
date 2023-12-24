from django.shortcuts import render


def home(request):
    return render(request, 'templates/home.html')


def catalog(request):
    return render(request, 'templates/contact.html')
