from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_travelbooking_contact_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="travelpackage",
            name="detailed_itinerary",
            field=models.TextField(blank=True),
        ),
    ]
