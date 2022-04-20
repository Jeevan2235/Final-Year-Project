from django.urls import path, include

from rest_framework.routers import DefaultRouter

from accounts.api import viewset


router = DefaultRouter()
router.register(
    "register-customer", viewset.RegisterUserView, basename="register-customer",
)
router.register(
    "register-staff", viewset.RegisterStaffView, basename="register-staff"
)
router.register(
    "profile", viewset.UserProfileView, basename="profile"
)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include('djoser.urls.jwt')),
]