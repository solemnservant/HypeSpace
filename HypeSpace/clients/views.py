from django.shortcuts import render
from .models import Client

# Create your views here.
def office(request, client_id):
    """Comapany page for updating facilities info"""
    client = Client.objects.get(id = client_id)
    location = Location.objects.get(id = location_id)
    lease = Lease.objects.get(id = lease_id)
    soft_serv = Soft_Services.objects.get(id = soft_services_id)
    hard_serv = Hard_Services.objects.get(id = hard_services_id)
    safety_serv = Safety_Services.objects.get(id = safety_services_id)
    context = {'client': client, 'location': location, 'lease': lease, 'soft_serv' : soft_services, 
               'hard_serv' : hard_services, 'safety_serv' : safety_services}
    return render(request, 'clients/office.html', context)

def all_clients(request):
    '''Shows list of all clients'''
    all_clients = Client.objects.orderby ('date_added')
    context = {'all_clients': all_cients}
    return render(request, 'clients/all_clients.html', context)

def index (request):
    """Test Page"""
    return render(request, 'clients/index.html')