from django.shortcuts import render
from django.http import HttpResponse

# Create your view0
# def index(request):
    # return HttpResponse("Hello, world. You're at the index of my potfolio.")

def index(request):
    template = "index.html"
    return  render(request, template, context=None)