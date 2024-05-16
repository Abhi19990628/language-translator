from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator 

def home(request): 
    if request.method == "POST": 
        text = request.POST.get("translate", "")  # Use get() method to avoid KeyError if 'translate' is not in POST data
        language = request.POST.get("language", "en")  # Default to English if 'language' is not provided

