from django.shortcuts import render



def tabel(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'index.html')