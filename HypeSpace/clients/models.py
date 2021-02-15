from django.db import models

# Create your models here.
class Client(models.Model):
    #A client is composed of the company general info
    text = models.CharField('Company Name',default = 'Company Name', max_length = 200)
    phone_num = models.CharField('Phone Number', default = '000-000-000', max_length = 12)
    ceo_name = models.CharField ('CEO', max_length = 50)
    num_employees = models.IntegerField('Number of Employees', default = 0)
    maintenance_schedule = models.CharField('maintenance schedule', max_length = 100)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Location(models.Model):
    #Location holds headquarters and satellite facilities info
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    text = models.CharField('Address', default = 'Address', max_length = 250)
    address2 = models.CharField('Address 2', max_length = 250)
    city = models.CharField(max_length = 250)
    state = models.CharField(max_length = 250)
    zipcode=models.IntegerField(default = 00000)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Lease(models.Model):
    #Leasing information for company's facilities
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    text = models.CharField('Leasee', default = 'Leasee', max_length = 150)
    rate = models.FloatField(default = 0.00)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateField('Start Date')

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Soft_Services(models.Model):
    #soft facility serives include items not related to physical facility
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    security_crew_title = models.CharField(max_length = 200)
    cleaning_crew_title = models.CharField(max_length = 200)
    landscaping_crew_title = models.CharField(max_length = 200)
    caterers = models.CharField(max_length = 200)

    def __str__(self):
        """Return a string represntation of the model."""
        return self.text
    
class Safety_Services(models.Model):
    #Safety services include items such as first aid training
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    training_schedule = models.DurationField('training schedule')
    audit_schedule = models.DurationField('audit schedule')
    saftety_meetings = models.DateTimeField ('meeting schedule')
    safety_coordinator = models.CharField(max_length = 150)
    job_safety_analysis = models.CharField (max_length = 500)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Hard_Services(models.Model): 
    #Hard services include overhead services such as utilities
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    electric_provider = models.CharField(max_length = 200)
    plumbing_provider = models.CharField(max_length = 200)
    hvac_provider = models.CharField(max_length = 200)
    mechanical_provider = models.CharField(max_length = 200)
    fire_safety_provider = models.CharField(max_length = 200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text