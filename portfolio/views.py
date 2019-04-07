from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your view0
# def index(request):
    # return HttpResponse("Hello, world. You're at the index of my potfolio.")

def index(request):
    with open('portfolio/akshat_context.json') as json_file:  
        data = json.load(json_file) 
    template = "index.html"
    return  render(request, template, context={"data":data, "range":range(5),})