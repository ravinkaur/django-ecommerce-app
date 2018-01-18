from django.conf.urls import patterns, url

from apps.appointment import views
from oscar.core.application import Application

     

class AppointmentApplication(Application):
    name = 'appointment'
               
    appointment_madrid = views.AppointmentMadrid
    appointment_sevilla = views.AppointmentSevilla
    
    def get_urls(self):
        urls = [
                url(r'cita-madrid',self.appointment_madrid.as_view(),name="appointment-madrid"),
                url(r'cita-sevilla',self.appointment_sevilla.as_view(),name="appointment-sevilla"),
                
        ]
        return self.post_process_urls(patterns('', *urls))


application = AppointmentApplication()