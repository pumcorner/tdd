from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):

    # templetes can be subsistuting python variables
    # we use render render_to_string rather than open (which opens file in disk) 

    # We have a multi dict key error here if using request.POST['item_text']
    # I guess that's because the default empty key is None and we actually get a '' in test one
    # Still confusing needs to look into doc
    return render(request,'home.html',{'new_item_text': request.POST.get('item_text',''),})
