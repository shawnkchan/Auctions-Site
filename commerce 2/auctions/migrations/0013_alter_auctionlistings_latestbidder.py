# Generated by Django 4.1.4 on 2022-12-23 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0012_alter_auctionlistings_latestbidder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auctionlistings",
            name="latestBidder",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bids",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
