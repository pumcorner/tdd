from django.shortcuts import render,redirect
from .models import Item,List

# Create your views here.

def home_page(request):

    ## templetes can be subsistuting python variables
    ## we use render render_to_string rather than open (which opens file in disk)

    ## We have a multi dict key error here if using request.POST['item_text']
    #(?) I guess that's because the default empty key is None and we actually get a '' in test one
    #(?) Still confusing needs to look into doc
    ## objects.create() equals item=Item() & item.save()
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html',{'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text = request.POST['item_text'],list = list_)
    return redirect('/lists/the-only-one-identifier/')
