from rest_framework import permissions

from core.infrastructure.choices import ADMIN, STAFF


class TicketFlightPermissions(permissions.BasePermission):
    """Only Allow Staff to update delete and create ticket"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role in [ADMIN, STAFF]


class ProfilePermissions(permissions.BasePermission):
    """Only Allow Users to Manage their own Profile"""
    
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False


class PurchasePermissions(permissions.BasePermission):
    """Only Allow Staffs to access all Purchases"""
    
    def has_permission(self, request, view):
        if request.user.role in [ADMIN, STAFF]:
            return True
        return False