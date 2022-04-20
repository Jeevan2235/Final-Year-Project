from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

from core.settings import EMAIL_HOST_USER
from tickets.models import Ticket, Flight
from accounts.models import User
from core.infrastructure import choices


class Booking(models.Model):
    """Database model for Booking Objects in the database"""

    booked_by = models.ForeignKey(
        User, related_name="user_bookings", on_delete=models.CASCADE
    )
    ticket = models.ForeignKey(
        Ticket, related_name="ticket_bookings", on_delete=models.CASCADE
    )


def book_ticket(sender, instance, created, *args, **kwargs):
    """function to set booked true in ticket after customer books"""

    if created:
        ticket = Ticket.objects.get(id=instance.ticket.id)
        ticket.booked = True
        ticket.save()


post_save.connect(book_ticket, sender=Booking)


class Purchase(models.Model):
    """Database model for Purchase Objects in the database"""

    passenger_name = models.CharField(max_length=255)
    passenger_gender = models.CharField(
        choices=choices.GENDER_TYPES, max_length=10, default=choices.MALE
    )
    passenger_document_type = models.CharField(
        choices=choices.DOCUMENT_TYPES, max_length=15, default=choices.CITIZENSHIP
    )
    passenger_document_number = models.CharField(max_length=55)
    passenger_nationality = models.CharField(
        choices=choices.NATIONALITIES_CHOICES, max_length=55, default="Nepalese"
    )
    contact_name = models.CharField(max_length=255)
    contact_gender = models.CharField(
        choices=choices.GENDER_TYPES, max_length=10, default=choices.MALE
    )
    contact_phone = models.CharField(max_length=14)
    contact_email = models.EmailField(max_length=255)
    ticket = models.ForeignKey(
        Ticket, related_name="purchase", on_delete=models.CASCADE
    )

    def get_total(self):
        return self.ticket.price.amount


def purchase_ticket(sender, instance, created, *args, **kwargs):
    """function to set purchased and booked true in ticket after customer purchase"""

    if created:
        ticket = Ticket.objects.get(id=instance.ticket.id)
        ticket.booked = True
        ticket.purchased = True
        ticket.save()


post_save.connect(purchase_ticket, sender=Purchase)


def send_cancellation_email(sender, instance, *args, **kwargs):
    """function to send email to users once flight has been cancelled"""

    if instance.cancelled:
        contact_emails = list(
            Purchase.objects.filter(ticket__flight=instance).values_list(
                "contact_email", flat=True
            )
        )
        send_mail(
            "FLIGHT CANCELLED",
            "SORRY YOUR FLIGHT HAS BEEN CANCELLED",
            EMAIL_HOST_USER,
            contact_emails,
        )


post_save.connect(send_cancellation_email, sender=Flight)
