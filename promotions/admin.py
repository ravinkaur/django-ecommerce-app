from django.contrib import admin
from apps.promotions.models import CarouselImage, CountDownEvent,EventThumb

admin.site.register(CarouselImage)
admin.site.register(CountDownEvent)
admin.site.register(EventThumb)
from oscar.apps.promotions.admin import *