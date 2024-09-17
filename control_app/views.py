from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def standby(request):
    return render(request, 'standby.html')

