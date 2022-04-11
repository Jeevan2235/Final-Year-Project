from decimal import Decimal
from django.db import models
from django.db.models.signals import post_save

from djmoney.models.fields import MoneyField


class Flight(models.Model):
    """Database model for flights"""
    
    flight_number = models.CharField(max_length=10)
    baggage_limit = models.CharField(max_length=10)
    flight_time = models.CharField(max_length=10)
    duration = models.CharField(max_length=55)
    departure_date = models.DateField()
    arrival_location = models.CharField(max_length=255)
    departure_location = models.CharField(max_length=255)
    cancelled = models.BooleanField(default=False)


class Ticket(models.Model):
    """Database model for tickets in the system"""
    
    ticket_class = models.CharField(max_length=10)
    seat_no = models.CharField(max_length=10)
    flight = models.ForeignKey(Flight, related_name="tickets", on_delete=models.CASCADE)
    price = MoneyField(default=0.00, default_currency='USD', max_digits=14, decimal_places=2)
    booked = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)
    refundable = models.BooleanField(default=False)
    
    def price_in_usd(self):
        return self.price/Decimal(121)


def create_tickets_for_flight(sender, instance, created, *args, **kwargs):
    """function to send create tickets automatically for flight"""
    
    if created:
        Ticket.objects.bulk_create(
            [Ticket(ticket_class='A',seat_no=f"{i+1}",flight=instance,price="3200.00",refundable=False) for i in range(12)]
        )
        Ticket.objects.bulk_create(
            [Ticket(ticket_class='B',seat_no=f"{i+1}",flight=instance,price="6400.00",refundable=True) for i in range(12)]
        )


post_save.connect(create_tickets_for_flight, sender=Flight)