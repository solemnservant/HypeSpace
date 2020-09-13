from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render   

def index(request):
    now = datetime.now()

    return render(
        request,
        "Landing_Page/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )