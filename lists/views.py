# from django.shortcuts import render
# from django.http import HttpResponse

# def home_page(request):
#     return HttpResponse('<html><title>To-Do lists</title></html>')

from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')