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

def view_list(request, list_id):
    list_ = List.objects.get(id = list_id)
    return render(request, 'list.html',{'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text = request.POST['item_text'],list = list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text = request.POST['item_text'], list = list_)
    return redirect(f'/lists/{list_.id}/')
