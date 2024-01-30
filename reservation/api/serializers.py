from rest_framework import serializers
from .models import Schedule, Booking


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        
class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'