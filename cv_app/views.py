from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.
def show_pdf(request):
    filepath = os.path.join('media', 'postylha.o-cv.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
