from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

import auctions

from .models import AuctionListings, User, AuctionBids, AuctionComments, Watchlist


def index(request):
    listings = AuctionListings.objects.all()
    
    return render(request, 'auctions/index.html', {
        'listings': listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
        bid = request.POST['startBid']
        image = request.POST['image']
        category = request.POST['category']
        user_id = User.objects.get(username=request.POST['user'])
        listing = AuctionListings(name=title, description=desc, seller=user_id, startBid=bid, imageUrl=image, categories=category)
        listing.save()
    return render(request, "auctions/create.html")

def listing(request, listing_id):
    listing = AuctionListings.objects.get(pk=listing_id)
    comments = listing.listComments.all()

    if request.method == 'POST':
        if 'bid' in request.POST:
            bid = int(request.POST['bid'])
            bidder = request.POST['bidder']
            if bid < listing.startBid:
                messages.error(request, 'Please enter a bid higher than the existing value')
            else:
                listing.startBid = bid
                listing.save(update_fields=['startBid'])
                listing.latestBidder = User.objects.get(username=bidder)
                listing.save(update_fields=['latestBidder'])
        elif 'status' in request.POST:
            status = request.POST['status']
            listing.status = status
            listing.save(update_fields=['status'])
        elif 'comment' in request.POST:
            comment = request.POST['comment']
            commenter = User.objects.get(username=request.POST['commenter'])
            newComment = AuctionComments(username=commenter, comment=comment, item=listing)
            newComment.save()
        else:
            item = AuctionListings.objects.get(id=request.POST['item'])
            user = User.objects.get(username=request.POST['user'])
            newItem = Watchlist(username=user, item=item)
            newItem.save()



    return render(request, 'auctions/listing.html', {
        'listing': listing,
        'comments': comments
    })


def watchlist(request, user_id):
    # Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
    userWatch = Watchlist.objects.filter(username=user_id)
    return render(request, 'auctions/watchlist.html', {
        'watchlist': userWatch
    })


def categories(request):
    categories = AuctionListings.objects.values_list('categories', flat=True).distinct()
    return render(request, 'auctions/categories.html', {
        'categories': categories
    })

def indexCats(request, category):
    listings = AuctionListings.objects.filter(categories=category)

    return render(request, 'auctions/index.html', {
        'listings': listings
    })

# """"NEED TO CHANGE ALL .USERNAME TO .ID!!!""""