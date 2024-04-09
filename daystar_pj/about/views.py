from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a_index(request):
    my_response = "This is the About Us page"
    respo = HttpResponse(my_response)
    return respo
