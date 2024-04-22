from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact

# Create your views here.

def contactindex(request):
    template = loader.get_template('contact.html')
    homeContent = template.render()
    return HttpResponse(homeContent) 
