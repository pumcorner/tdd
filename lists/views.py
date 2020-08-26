from django.shortcuts import render,redirect
from .models import Item

# Create your views here.

def home_page(request):

    # templetes can be subsistuting python variables
    # we use render render_to_string rather than open (which opens file in disk) 

    # We have a multi dict key error here if using request.POST['item_text']
    # I guess that's because the default empty key is None and we actually get a '' in test one
    # Still confusing needs to look into doc
    if request.method == 'POST':
        # objects.create() equals item=Item() & item.save()
        Item.objects.create(text = request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html',{'items': items})
