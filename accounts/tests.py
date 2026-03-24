from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import TravelBooking, TravelPackage


class PackageBookingFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="traveler@example.com",
            email="traveler@example.com",
            password="pass12345",
        )
        self.package = TravelPackage.objects.create(
            title="Goa Escape",
            duration=5,
            price="25000.00",
            short_description="Beach holiday",
            detailed_itinerary="Day 1: Arrival in Goa\nDay 2: Baga Beach and Fort Aguada",
            places_included="Baga Beach, Fort Aguada, Dudhsagar",
            inclusions="Hotel, breakfast, transfers",
            trip_type="Leisure trip",
            payment_details="Pay 30% advance by UPI to confirm the slot.",
        )

    def test_package_detail_preview_requires_login_for_full_trip_details(self):
        response = self.client.get(reverse("package_detail", args=[self.package.id]))

        self.assertContains(response, "Beach holiday")
        self.assertContains(response, "Login to See Full Details")
        self.assertNotContains(response, "Baga Beach, Fort Aguada, Dudhsagar")
        self.assertNotContains(response, "Day 1: Arrival in Goa")

    def test_logged_in_user_sees_admin_added_full_trip_details(self):
        self.client.login(username="traveler@example.com", password="pass12345")

        response = self.client.get(reverse("package_detail", args=[self.package.id]))

        self.assertContains(response, "Baga Beach, Fort Aguada, Dudhsagar")
        self.assertContains(response, "Day 1: Arrival in Goa")
        self.assertContains(response, "Pay 30% advance by UPI to confirm the slot.")

    def test_logged_in_user_can_create_booking_with_payment_method(self):
        self.client.login(username="traveler@example.com", password="pass12345")

        response = self.client.post(
            reverse("book_package", args=[self.package.id]),
            {
                "traveler_count": 3,
                "travel_date": "2026-05-10",
                "contact_number": "9876543210",
                "payment_method": TravelBooking.PAYMENT_METHOD_UPI,
                "special_requests": "Need airport pickup",
            },
        )

        self.assertRedirects(response, reverse("package_detail", args=[self.package.id]))
        booking = TravelBooking.objects.get(user=self.user, package=self.package)
        self.assertEqual(booking.traveler_count, 3)
        self.assertEqual(booking.payment_status, TravelBooking.PAYMENT_STATUS_PENDING)
        self.assertEqual(booking.payment_method, TravelBooking.PAYMENT_METHOD_UPI)

    def test_booking_requires_all_fields_including_travel_date(self):
        self.client.login(username="traveler@example.com", password="pass12345")

        response = self.client.post(
            reverse("book_package", args=[self.package.id]),
            {
                "traveler_count": "",
                "travel_date": "",
                "contact_number": "",
                "payment_method": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.", count=4)
        self.assertFalse(
            TravelBooking.objects.filter(user=self.user, package=self.package).exists()
        )

    def test_booking_rejects_past_travel_date(self):
        self.client.login(username="traveler@example.com", password="pass12345")

        response = self.client.post(
            reverse("book_package", args=[self.package.id]),
            {
                "traveler_count": 2,
                "travel_date": (timezone.localdate() - timedelta(days=1)).isoformat(),
                "contact_number": "9876543210",
                "payment_method": TravelBooking.PAYMENT_METHOD_UPI,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Travel date cannot be earlier than today.")
        self.assertFalse(
            TravelBooking.objects.filter(user=self.user, package=self.package).exists()
        )
