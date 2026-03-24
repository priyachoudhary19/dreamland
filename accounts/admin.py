from django.contrib import admin
from .models import Author, TravelBooking, TravelPackage, registration


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tagline")


@admin.register(registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "mobile", "address")
    search_fields = ("name", "email", "mobile")


@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration", "price", "is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("title", "short_description", "detailed_itinerary")
    ordering = ("sort_order", "id")


@admin.register(TravelBooking)
class TravelBookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "package", "booked_at")
    list_filter = ("booked_at",)
    search_fields = ("user__username", "package__title")
