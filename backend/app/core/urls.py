from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('tickets/', include('tickets.urls')),
    path('bookings/', include('bookings.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
