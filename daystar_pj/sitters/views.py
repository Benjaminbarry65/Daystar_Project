from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sitter

# Create your views here.
#create view functions for CRUD.

def sitterHome(request):
    if request.method == 'POST':
        submitted_name = request.POST('name')
        allsitters = Sitters.objects.filter(name=submitted_name)
    else:    
        allsitters = Sitter.objects.all()
    context = {
        'allsitters': allsitters
    }
    template = loader.get_template('sitters.html')
    return HttpResponse(template.render(context))

def addSitter(request):
    message = None
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        date_admitted = request.POST['date']
        contact = request.POST['contact']
        sitter_obj = Sitter.objects.create(name=name, gender=dender, date_admitted=date_admitted, contact=contact)
        sitter_obj.save()
        message = "Sitter Added Successfully"
    context = {
        'message': message
    }
    template = loader.get_template('addsitter.html')
    return HttpResponse(template.render(context))

def editSitter(request):
    template = loader.get_template('editsitter.html')
    return HttpResponse(template.render())

def deleteSitter(request):
    template = loader.get_template('deletesitter.html')
    return HttpResponse(template.render())

def readSitter(request):
    template = loader.get_template('readsitter.html')
    return HttpResponse(template.render())                