from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bookings.api import viewset


router = DefaultRouter()
router.register(
    "book-ticket", viewset.BookTicketViewSet, basename="book-ticket",
)
router.register(
    "current-bookings", viewset.CurrentBookingsViewSet, basename="current-bookings",
)
router.register(
    "all-bookings", viewset.AllBookingsViewSet, basename="all-bookings",
)
router.register(
    "purchase-ticket", viewset.PurchaseTicketViewSet, basename="purchase-ticket",
)
router.register(
    "current-purchases", viewset.CurrentPurchasesViewSet, basename="current-purchases",
)
router.register(
    "all-purchases", viewset.AllPurchasesViewSet, basename="all-purchases",
)


urlpatterns = [
    path("", include(router.urls)),
    path("cancel-booking/<int:booking_id>/", viewset.CancelBookingView.as_view()),
    path('process-payment/<int:purchase_id>/', viewset.process_payment, name='process_payment'),
]