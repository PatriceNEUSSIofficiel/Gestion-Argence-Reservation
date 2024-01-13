from rest_framework import serializers
from .models import Schedule


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'