# Generated by Django 4.1.4 on 2022-12-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlistings",
            name="startBid",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
