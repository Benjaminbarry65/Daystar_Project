from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wel_index(request):
    my_response = "Welcome to Daystar Daycare"
    respon = HttpResponse(my_response)
    return respon