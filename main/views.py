from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator 

def home(request): 
    if request.method == "POST": 
        text = request.POST.get("translate", "")  # Use get() method to avoid KeyError if 'translate' is not in POST data
        language = request.POST.get("language", "en")  # Default to English if 'language' is not provided
          if text:  # Check if text is not empty
            translator = Translator(to_lang=language)
            try:
                translation = translator.translate(text)
                return HttpResponse(translation)
            except Exception as e:
                # Handle translation errors here, e.g., log the error or return an error message
                return HttpResponse(f"Translation Error: {str(e)}", status=500)
        else:
            return HttpResponse("No text to translate", status=400)  # Return a 400 Bad Request status if no text provided
    else:
        return render(request, "main/index.html")  # Render the template for GET requests

