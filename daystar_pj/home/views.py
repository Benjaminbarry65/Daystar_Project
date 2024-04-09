from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_response = "Hello, This is the Daystar Daycare"
    resp = HttpResponse(my_response)
    return resp
