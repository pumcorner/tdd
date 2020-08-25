from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):

    # templetes can be subsistuting python variables
    # we use render render_to_string rather than open (which opens file in disk) 
    return render(request, 'home.html')
