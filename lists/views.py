# from django.shortcuts import render
# from django.http import HttpResponse

# def home_page(request):
#     return HttpResponse('<html><title>To-Do lists</title></html>')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    return render(request, 'home.html')

def view_list(request): 
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-new-page/')