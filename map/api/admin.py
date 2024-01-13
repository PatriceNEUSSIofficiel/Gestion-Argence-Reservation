from django.contrib import admin
from api.models import Category, Location, Bus, Schedule, Booking, Paiement
# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Booking)
admin.site.register(Paiement)
