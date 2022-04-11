from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from tickets.api import serializers
from tickets import models
from core.infrastructure.check_permissions import TicketFlightPermissions


class FlightViewSet(viewsets.ModelViewSet):
    """API Views for Handling Flights in the System"""
    
    queryset = models.Flight.objects.all()
    serializer_class = serializers.FlightSerializer
    permission_classes = (TicketFlightPermissions,)


class TicketViewSet(viewsets.ModelViewSet):
    """API Views for Handling Tickets in the System"""
    
    serializer_class = serializers.TicketSerializer
    permission_classes = (TicketFlightPermissions,)
    
    def get_queryset(self):
        return models.Ticket.objects.filter(booked=False,flight__cancelled=False)


class FilteredTicketViewSet(viewsets.ModelViewSet):
    """API Views for Handling User Requested Tickets in the System"""
    
    queryset = models.Ticket.objects.filter(booked=False,flight__cancelled=False)
    serializer_class = serializers.TicketSerializer
    http_method_names = ['get',]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        filter_names = ['departure_location', 'arrival_location', 'departure_date']
        filters = {}
        for key, value in self.request.query_params.items():
            if key in filter_names:
                filters[key] = value
        if len(filters):
            flight = models.Flight.objects.filter(**filters)
            return models.Ticket.objects.filter(flight__in=flight,booked=False,flight__cancelled=False)
        return models.Ticket.objects.filter(booked=False,flight__cancelled=False)