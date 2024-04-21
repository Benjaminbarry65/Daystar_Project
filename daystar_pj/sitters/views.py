from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#create view functions for CRUD.

def sitterHome(request):
    template = loader.get_template('sitters.html')
    return HttpResponse(template.render())

def addSitter(request):
    template = loader.get_template('addsitter.html')
    return HttpResponse(template.render())

def editSitter(request):
    template = loader.get_template('editsitter.html')
    return HttpResponse(template.render())

def deleteSitter(request):
    template = loader.get_template('deletesitter.html')
    return HttpResponse(template.render())

def readSitter(request):
    template = loader.get_template('readsitter.html')
    return HttpResponse(template.render())                