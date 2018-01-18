from oscar.apps.promotions.models import AbstractPromotion
from django.db import models
from django.conf import settings
from oscar.models.fields import ExtendedURLField
from django.utils.translation import ugettext_lazy as _

class CarouselImage(AbstractPromotion):
    """
    
    """
    _type = 'CarouselImage'
    name = models.CharField(_("Name"), max_length=128)
    url = ExtendedURLField(
        _('url'), max_length=128, db_index=True, verify_exists=True)
    image = models.ImageField(
        _('Image'), upload_to=settings.OSCAR_PROMOTION_FOLDER,
        max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(_("HTML message"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Carousel Image")
        verbose_name_plural = _("Carousel Images")


class CountDownEvent(AbstractPromotion):
    """
    For events
    """
    _type = 'CountDownEvent'
    heading = models.CharField(_("Heading"), max_length=128)
    subheading = models.CharField(_("Subheading"), max_length=128,blank=True, null=True)
    image = models.ImageField(
        _('Image'), upload_to=settings.OSCAR_PROMOTION_FOLDER,
        max_length=255)
    date = models.DateTimeField(_("Date"))
    
    def __unicode__(self):
        return self.heading + str(self.date)
    
    class Meta:
        verbose_name = _("CountDownEvent")
        verbose_name_plural = _("CountDownEvents")
        
        
class EventThumb(AbstractPromotion):
        
    _type= 'EventThumb'
    name = models.CharField(_("Name"), max_length=128)
    address = models.CharField(_("Address"), max_length=128)
    days = models.CharField(_("Days"), max_length=128)
    month = models.CharField(_("Month"), max_length=128)
    description = models.TextField(_("Description"))
    address = models.CharField(_("Address"), max_length=128)
    schedule = models.CharField(_("Schedule"), max_length=128)
    thumb = models.ImageField(
        _('Image'), upload_to=settings.OSCAR_PROMOTION_FOLDER,
        max_length=255)
    map_link = models.CharField(_("Map Link"), max_length=128)
    map_iframe = models.TextField(_("Map iframe"))
    
    def __unicode__(self):
        return self.name 
    
    class Meta:
        verbose_name = _("EventThumb")
        verbose_name_plural = _("EventsThumb")    
    
from oscar.apps.promotions.models import *