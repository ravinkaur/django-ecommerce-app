
from django.contrib import admin
from apps.appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('mail', 'date_created')
    

admin.site.register(Appointment, AppointmentAdmin)
