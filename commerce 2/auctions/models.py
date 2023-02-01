from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListings(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    categories = models.CharField(max_length=1000, default='')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', null=True)
    startBid = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    imageUrl = models.URLField(max_length=400, default='')
    latestBidder= models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids', null=True)
    status = models.IntegerField(default=1)
    # watchers = models.ManyToManyField(User, related_name='watching')


    def __str__(self) -> str:
        return f"{self.name}, listed on: {self.date}"

class AuctionBids(models.Model):
    bid = models.DecimalField(max_digits=20, decimal_places=2)
    item = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name='listingBids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userBids')

    def __str__(self) -> str:
        return f"{self.bid}"

class AuctionComments(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userComments')
    comment = models.CharField(max_length=100)
    item = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name='listComments')

class Watchlist(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    item = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name='watch')
