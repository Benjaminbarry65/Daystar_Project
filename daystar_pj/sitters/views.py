from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#create view functions for CRUD.

def sitterHome(request):
    return HttpResponse("sitterHome")

def addSitter(request):
    return HttpResponse("addSitter")

def editSitter(request):
    return HttpResponse("editSitter")

def deleteSitter(request):
    return HttpResponse("deleteSitter")

def readSitter(request):
    return HttpResponse("readSitter")                