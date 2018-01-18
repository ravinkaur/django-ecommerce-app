from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.models.fields import PhoneNumberField
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
import logging
from smtplib import SMTPException


logger = logging.getLogger('appointment.mailing')

class Appointment(models.Model):
    
    
    name = comments = models.CharField(_("Nombre"),max_length=100,blank=True)
     
    mail = models.EmailField(_("Mail"))
    
    phone = PhoneNumberField(_("Telefono"))
    
    comments = models.TextField(_("Comentarios"), blank=True)    
    
    date = models.DateField(_('Fecha cita'))
    MADRID, SEVILLA, BARCELONA = (
        "Madrid", "Sevilla", "Barcelona")
    CITY_CHOICES = (
        (MADRID, _("Madrid")),
        (SEVILLA, _("Sevilla")),
        (BARCELONA, _("Barcelona")),
    )
    city = models.CharField(
        _("City"), max_length=128, default=MADRID, choices=CITY_CHOICES)
    
    date_created = models.DateTimeField(_('date created'),auto_now_add=True)
    
    url_source = models.TextField(_("Url"), blank=True)
    
    subject_intro = settings.APPOINTMENT_SUBJECT
    from_email = settings.APPOINTMENT_FROM
    email_recipients = settings.APPOINTMENT_EMAIL_RECIPIENTS
    template_name = 'customer/appointment/mail/email_body.txt'
    html_template_name = 'customer/appointment/mail/email_body.html'
    
      
    
    class Meta:
        ordering = ['-date_created']
        
    def __unicode__(self):
        return '"%s": "%s"' % (self.date_created, self.mail)
    
    
    def send_mail(self):
        subject = self.get_subject()
        from_email = self.get_from_email()
        email_recipients = self.get_email_recipients()
        context = self.get_context()
        message_body = render_to_string(self.get_template_names(), context)
        try:
            message = mail.EmailMultiAlternatives(
                subject=subject,
                body=message_body,
                from_email=from_email,
                to=email_recipients,
                headers={
                    'Reply-To': self.mail
                }
            )
            html_body = render_to_string(self.html_template_name, context)
            message.attach_alternative(html_body, "text/html")
            message.send()
            logger.info(_("Appointment form submitted and sent (from: %s)") %
                        self.mail)
        except SMTPException:
            logger.exception(_("An error occured while sending the email"))
            return False
        else:
            return True
    def get_context(self):
        ctx = {}
        ctx['mail'] = self.mail
        ctx['name'] = self.name
        ctx['phone'] = self.phone
        ctx['date'] = self.date
        ctx['comments'] = self.comments
        ctx['city'] = self.city
        return ctx 

    def get_subject(self):
        """
        Returns a string to be used as the email subject.
        Override this method to customize the display of the subject.
        """
        return self.subject_intro + self.mail

    def get_from_email(self):
        """
        Returns the from email address.
        Override to customize how the from email address is determined.
        """
        return self.from_email

    def get_email_recipients(self):
        """
        Returns a list of recipients for the message.
        Override to customize how the email recipients are determined.
        """
        return self.email_recipients

    def get_template_names(self):
        """
        Returns a template_name (or list of template_names) to be used
        for the email message.
        Override to use your own method choosing a template name.
        """
        return self.template_name
        