from django import forms

from .models import TravelPackage


class TravelPackageForm(forms.ModelForm):
    class Meta:
        model = TravelPackage
        fields = [
            "title",
            "duration",
            "price",
            "image",
            "short_description",
            "is_active",
            "sort_order",
        ]
        widgets = {
            "short_description": forms.Textarea(attrs={"rows": 3}),
        }
