from django.contrib import admin
from bookings import models

# Register your models here.
admin.site.register(models.Booking)
admin.site.register(models.Purchase)