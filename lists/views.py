# from django.shortcuts import render
# from django.http import HttpResponse

# def home_page(request):
#     return HttpResponse('<html><title>To-Do lists</title></html>')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-new-page/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def view_list(request): 
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
