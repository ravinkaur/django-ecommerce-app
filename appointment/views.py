from apps.appointment.models import Appointment
from apps.appointment.forms import AppointmentForm, AppointmentFooterForm
from oscar.apps.customer.mixins import PageTitleMixin
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from apps.appointment.tasks import send_mail as send_mail_task
from django.http import HttpResponseRedirect
from rest_framework.generics import CreateAPIView
from apps.appointment.serializers import AppointmentBotRestSerializer

class AppointmentCreateView(generic.CreateView):
    form_class = AppointmentForm
    model = Appointment
    template_name = 'customer/appointment/madrid.html'
    success_url = '/trajes-camisas-a-medida-madrid/#cita'
    
    def form_valid(self, form):
        messages.success(self.request, self.get_success_message(form))
        self.object = form.save()
        send_mail_task.delay(self.object.id)
        return HttpResponseRedirect(self.get_success_url())

    
    def get_success_message(self, form):        
        return render_to_string(
            'customer/appointment/messages/add_appointment.html',
            {'date': form.cleaned_data['date'],
             'mail': form.cleaned_data['mail']})



class AppointmentMadrid(AppointmentCreateView):
    template_name = 'customer/appointment/madrid.html'
    success_url = '/trajes-camisas-a-medida-madrid/#cita'

# edited

# #footer_form
class AppointmentCreateFooterView(generic.CreateView):
    form_class = AppointmentFooterForm
    model = Appointment
    template_name = 'customer/appointment/madrid-hombre.html'
    success_url = '/trajes-a-medida-Madrid-hombre/#cita'
    
    def form_valid(self, form):
        messages.success(self.request, self.get_success_message(form))
        self.object = form.save()
        send_mail_task.delay(self.object.id)
        return HttpResponseRedirect(self.get_success_url())

    
    def get_success_message(self, form):        
        return render_to_string(
            'customer/appointment/messages/add_appointment.html',
            {'date': form.cleaned_data['date'],
             'mail': form.cleaned_data['mail']})

class AppointmentMadridHome(AppointmentCreateView):
    template_name = 'customer/appointment/madrid-hombre.html'
    success_url = '/trajes-a-medida-Madrid-hombre/#cita'

class AppointmentSuitMadrid(AppointmentCreateView):
    template_name = 'customer/appointment/trajes-novios-madrid.html'
    success_url = '/trajes-novio-a-medida-Madrid-hombre/'

# //edited 

class AppointmentSevilla(AppointmentCreateView):
    template_name = 'customer/appointment/sevilla.html'
    success_url = '/trajes-camisas-a-medida-sevilla/#cita'    
    
class AppointmentBarcelona(AppointmentCreateView):
    template_name = 'customer/appointment/barcelona.html'
    success_url = '/trajes-camisas-a-medida-barcelona/#cita'

class AppointmentJacketMadrid(AppointmentCreateView):
    template_name = 'customer/appointment/jacket-madrid.html'
    success_url = '/americanas-a-medida-madrid/#cita'


class AppointmentJacketSevilla(AppointmentCreateView):
    template_name = 'customer/appointment/jacket-sevilla.html'
    success_url = '/americanas-a-medida-sevilla/#cita'


class AppointmentJacketBarcelona(AppointmentCreateView):
    template_name = 'customer/appointment/jacket-barcelona.html'
    success_url = '/americanas-a-medida-barcelona/#cita'

class AppointmentPantsMadrid(AppointmentCreateView):
    template_name = 'customer/appointment/pants-madrid.html'
    success_url = '/pantalones-a-medida-madrid/#cita'


class AppointmentPantsSevilla(AppointmentCreateView):
    template_name = 'customer/appointment/pants-sevilla.html'
    success_url = '/pantalones-a-medida-sevilla/#cita'


class AppointmentPantsBarcelona(AppointmentCreateView):
    template_name = 'customer/appointment/pants-barcelona.html'
    success_url = '/pantalones-a-medida-barcelona/#cita'

class AppointmentVestMadrid(AppointmentCreateView):
    template_name = 'customer/appointment/vest-madrid.html'
    success_url = '/chalecos-a-medida-madrid/#cita'


class AppointmentVestSevilla(AppointmentCreateView):
    template_name = 'customer/appointment/vest-sevilla.html'
    success_url = '/chalecos-a-medida-sevilla/#cita'


class AppointmentVestBarcelona(AppointmentCreateView):
    template_name = 'customer/appointment/vest-barcelona.html'
    success_url = '/chalecos-a-medida-barcelona/#cita'

class AppointmentLinenMadrid(AppointmentCreateView):
    template_name = 'customer/appointment/linen-madrid.html'
    success_url = '/camisas-de-lino-a-medida-madrid/#cita'


class AppointmentLinenSevilla(AppointmentCreateView):
    template_name = 'customer/appointment/linen-sevilla.html'
    success_url = '/camisas-de-lino-a-medida-sevilla/#cita'


class AppointmentLinenBarcelona(AppointmentCreateView):
    template_name = 'customer/appointment/linen-barcelona.html'
    success_url = '/camisas-de-lino-a-medida-barcelona/#cita'


class AppointmentBotRestView(CreateAPIView):
    serializer_class = AppointmentBotRestSerializer
    def post(self, request, *args, **kwargs):
        response = super(AppointmentBotRestView, self).post(request, *args, **kwargs)
        print response.data
        send_mail_task.delay(response.data['id'])
        return response
    
    
     
















