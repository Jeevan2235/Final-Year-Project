from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tickets.api import viewset


router = DefaultRouter()
router.register(
    "flight",
    viewset.FlightViewSet,
    basename="flight",
)
router.register(
    "ticket",
    viewset.TicketViewSet,
    basename="ticket",
)
router.register(
    "filtered-ticket",
    viewset.FilteredTicketViewSet,
    basename="filtered-ticket",
)

urlpatterns = [
    path("", include(router.urls)),
]
