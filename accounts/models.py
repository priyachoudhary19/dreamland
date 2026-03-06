from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()


class registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class TravelPackage(models.Model):
    title = models.CharField(max_length=120)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="packages/", blank=True, null=True)
    image_url = models.URLField(blank=True)
    short_description = models.CharField(max_length=220, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title


class TravelBooking(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "package")
        ordering = ["-booked_at"]

    def __str__(self):
        return f"{self.user.username} - {self.package.title}"
