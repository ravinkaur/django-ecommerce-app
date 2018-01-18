from rest_framework import serializers
from apps.appointment.models import Appointment

class AppointmentBotRestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Appointment
        fields = ('id', 'name', 'mail', 'phone', 'comments', 'date', 'city')
        read_only = ('id')