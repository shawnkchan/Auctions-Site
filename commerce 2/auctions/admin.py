from django.contrib import admin
from .models import User, AuctionBids, AuctionComments, AuctionListings, Watchlist

# Register your models here.
class AuctionListingsAdmin(admin.ModelAdmin):
    list_display = ('id','startBid', 'date', 'name', 'description', 'categories', 'seller', 'latestBidder', 'status')

class AuctionBidsAdmin(admin.ModelAdmin):
    list_display = ('id', 'bid','item', 'user')

class AuctionCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','comment', 'item')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'item')

admin.site.register(User, UserAdmin)
admin.site.register(AuctionListings, AuctionListingsAdmin)
admin.site.register(AuctionBids, AuctionBidsAdmin)
admin.site.register(AuctionComments, AuctionCommentsAdmin)
admin.site.register(Watchlist, WatchlistAdmin)