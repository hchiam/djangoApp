from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# This is the simplest view possible in Django.
# To call this view, we need to map it to a URL - and this requires a URLconf.
# To create a URLconf in the polls directory, we need a file called urls.py