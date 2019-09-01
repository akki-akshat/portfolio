from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your view0
# def index(request):
    # return HttpResponse("Hello, world. You're at the index of my potfolio.")

def index(request):
    # with open('https://api.mlab.com/api/1/databases/sap_intro/collections/akki?apiKey=uRF8yptjRhXgGAK3wUNUrOawnwcK4tzV') as json_file:  
    data = requests.get('http://akshatahuja-eval-test.apigee.net/myintro').json()
    template = "index.html"
    return  render(request, template, context={"data":data[0]})