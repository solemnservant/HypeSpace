from django.shortcuts import render

# Create your views here.
def office(request):
    """Comapany page for updating facilities info"""
    return render(request, 'clients/office.html')

def index (request):
    """Test Page"""
    return render(request, 'clients/index.html')