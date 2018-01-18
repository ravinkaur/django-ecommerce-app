from django import forms
from django.forms import ModelForm
from apps.appointment.models import Appointment
from oscar.forms import widgets
from django.utils.translation import ugettext_lazy as _

class AppointmentForm(ModelForm):
    
    class Meta:
        model = Appointment
        exclude = ('date_created',)
        
        datetime = forms.DateField(input_formats='%d/%m/%Y',
        label=_("End datetime"), widget=widgets.DateTimePickerInput())
        

class AppointmentFooterForm(ModelForm):
    
    class Meta:
        model = Appointment
        exclude = ('date_created',)
        
        datetime = forms.DateField(input_formats='%d/%m/%Y',
        label=_("End datetime"), widget=widgets.DateTimePickerInput())