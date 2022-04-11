from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tickets.api import viewset
from .api.flight import FlightListAPI


router = DefaultRouter()
router.register(
    "flight", viewset.FlightViewSet, basename="flight",
)
router.register(
    "ticket", viewset.TicketViewSet, basename="ticket",
)
router.register(
    "filtered-ticket", viewset.FilteredTicketViewSet, basename="filtered-ticket",
)

urlpatterns = [
    path("flightlist", FlightListAPI.as_view(),name="flights_list"),
    path("", include(router.urls)),
]