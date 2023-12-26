from django.shortcuts import render
from django.template.loader import get_template
from .settings import BASE_DIR
import os

def home_page(request):
    print(BASE_DIR)
    print(os.path.join(BASE_DIR,'templates'))
    
    title = "Hello there..."
    context = {"title": title, "my_list": [1,2,3,4]}
    return render(request, "home.html",context)

def login(request):
    template_name = "login.html"
    context = {}
    render(request, template_name, context)