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


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include('djoser.urls.jwt')),
    path("profile/", viewset.UserProfileView.as_view({ 'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
     }),name="profile"), path("logout/",viewset.logout_user,name="logout")
]