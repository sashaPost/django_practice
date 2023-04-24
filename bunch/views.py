from django.shortcuts import render
from django.http import HttpResponse

def maintenance_mode(request):
    return render(request, 'bunch/maintenance.html')
