from django.contrib import admin
from tickets import models

# Register your models here.
admin.site.register(models.Ticket)
admin.site.register(models.Flight)