from __future__ import absolute_import

from celery import shared_task
from apps.appointment.models import Appointment
from django.core.exceptions import ObjectDoesNotExist



@shared_task
def send_mail(appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.send_mail()
        
    except ObjectDoesNotExist:
        return "Error: appointment %s does not exists" % appointment_id