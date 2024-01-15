from re import I
from unicodedata import category
from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum

class Email(models.Model):
    sender = models.EmailField()
    receiver = models.EmailField()
    subject = models.CharField(max_length=300)
    body = models.TextField()
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

class Bus(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank= True, null = True)
    bus_number = models.CharField(max_length=250)
    seats = models.FloatField(max_length=5, default=0)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_number

class Schedule(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE, null=True, blank=True)
    depart = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='depart_location', null=True, blank=True)
    destination = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='destination', null=True, blank=True)
    schedule= models.DateTimeField(null=True, blank=True)
    fare= models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled')), default=1, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        # return str(self.code + ' - ' + self.bus.bus_number) 
        return self.code



    def count_available(self):
        booked = Booking.objects.filter(schedule=self).aggregate(Sum('seats'))['seats__sum']
        return self.bus.seats - booked
    
     
        
    def nbrePlace(self):
            return self.bus.seats

class Booking(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    seats = models.IntegerField()
    status = models.CharField(max_length=2, choices=(('1','Pending'),('2','Paid')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code + ' - ' + self.name)

    def total_payable(self):
        return self.seats * self.schedule.fare

class Paiement(models.Model):
    
    email = models.EmailField()
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    
 
    

# @receiver(models.signals.post_save, sender=Invoice_Item)
# def stock_update(sender, instance, **kwargs):
#     stock = Stock(product = instance.product, quantity = instance.quantity, type = 2)
#     stock.save()
#     # stockID = Stock.objects.last().id
#     Invoice_Item.objects.filter(id= instance.id).update(stock=stock)

# @receiver(models.signals.post_delete, sender=Invoice_Item)
# def delete_stock(sender, instance, **kwargs):
#     try:
#         stock = Stock.objects.get(id=instance.stock.id).delete()
#     except:
#         return instance.stock.id



    
    