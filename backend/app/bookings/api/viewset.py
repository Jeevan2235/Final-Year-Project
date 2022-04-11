from django.shortcuts import get_object_or_404, render, redirect

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from bookings.api import serializers
from bookings import models
from core.infrastructure.check_permissions import PurchasePermissions


class BookTicketViewSet(viewsets.ModelViewSet):
    """API Views for Booking Tickets in the System"""
    
    serializer_class = serializers.BookingSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["post"]


class CurrentBookingsViewSet(viewsets.ModelViewSet):
    """API Views for Getting Booked Tickets in the System"""
    
    serializer_class = serializers.BookingSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get"]
    
    def get_queryset(self):
        return models.Booking.objects.filter(booked_by=self.request.user)


class AllBookingsViewSet(viewsets.ModelViewSet):
    """API Views for Getting All Booked Tickets in the System"""
    
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = (IsAuthenticated, PurchasePermissions)
    http_method_names = ["get"]


class PurchaseTicketViewSet(viewsets.ModelViewSet):
    """API Views for Purchasing Tickets in the System"""
    
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]
    
    def create(self, request, *args, **kwargs):
        serializer = serializers.PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            purchase = serializer.save()
            purchase_id = purchase.id
            request.session['purchase_id'] = purchase_id
            return redirect('process_payment')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentPurchasesViewSet(viewsets.ModelViewSet):
    """API Views for Getting Purchased Tickets in the System"""
    
    serializer_class = serializers.PurchaseSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get"]
    
    def get_queryset(self):
        return models.Purchase.objects.filter(contact_email=self.request.user.email)


class AllPurchasesViewSet(viewsets.ModelViewSet):
    """API Views for Getting All Purchased Tickets in the System"""
    
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    permission_classes = (IsAuthenticated, PurchasePermissions)
    http_method_names = ["get"]


class CancelBookingView(APIView):
    """API View for Cancelling Booking"""
    
    permission_classes = (IsAuthenticated,)

    def post(self, request, booking_id, format=None):
        booking = models.Booking.objects.filter(id=booking_id).first()
        if booking:
            booking.ticket.booked = False
            booking.ticket.save()
            booking.save()
            return Response({"message":"Booking Cancelled SuccessFully"}, status=status.HTTP_200_OK)
        return Response({"message":"Booking Does Not Exist"}, status=status.HTTP_400_BAD_REQUEST)


def process_payment(request):
    # getting purchase data from db
    purchase_id = request.session.get('purchase_id')
    purchase = get_object_or_404(models.Purchase, id=purchase_id)
    return render(request, 'process_payment.html', {'amount': purchase.ticket.price.amount})