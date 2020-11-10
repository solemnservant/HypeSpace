from django.contrib import admin

# Register your models here.
from .models import Client, Safety_Services, Soft_Services, Hard_Services, Location, Lease

admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Lease)
admin.site.register(Safety_Services)
admin.site.register(Soft_Services)
admin.site.register(Hard_Services)