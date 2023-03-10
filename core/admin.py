"""
Django admin customization
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for our users"""
    ordering = ["id"]
    list_display = ["email", "first_name", "last_name"]
    fieldsets = (
        (None, {"fields": ("email", "password"), }),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),

    )
    readonly_fields = ["last_login", "date_joined"]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "first_name",
                "last_name",
                "password1",
                "password2",
                "is_active",
                "is_staff",
                "is_superuser"
            )
        }),
    )
