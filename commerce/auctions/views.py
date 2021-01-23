from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import User, Item, Category, Comment, Bid, Watchlist
from .forms import ItemForm, BidForm, CommentForm
def index(request):
    return render(request, "auctions/index.html",{
        'Items':  Item.objects.all(),
        'Categories': Category.objects.all(),
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
'''
Create Listing:     Users should be able to visit a page to create a new listing. 
                    They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. 
                    Users should also optionally be able to provide a URL for an image for the listing 
                (I am using a FILE request, I think it is more complex and more similar to real eBay site)
                and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
'''

@login_required(login_url='/login')
def list(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owners = request.user
            new.prices = new.initial_bid
            new.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                "form": form,
            })
    else: 
        form = ItemForm()
        return render(request, 'auctions/create.html', {
            'form': form,
            })

def item(request, item_id):
    item = Item.objects.get(pk=item_id)
    comments = Comment.objects.filter(items=item_id)
    bids = Bid.objects.filter(items=item_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.POST.get("button") == "new_bid":
                form = BidForm(request.POST)
                if form.is_valid():
                    new = form.save(commit=False)
                    if (item.prices < new.bids):
                        new.users = request.user
                        new.items = item
                        new.save()
                        item.prices = new.bids
                        item.save()
                        return HttpResponseRedirect(f"{item.id}")
                    else: 
                        return render(request, 'auctions/item.html',{
                            'item': item,
                            'BidForm': BidForm(request.POST),
                            'CommentForm': CommentForm(request.POST),
                            'Comments': comments,
                            'message': "Your bid must be bigger than the current price.",
                            'Bids': bids
                        })
                else: 
                    # error
                    return render('auctions/item.html', {
                        'message': "",
                        'BidForm': BidForm(request.POST)
                    })
            if request.POST.get("button") == "comment":
                form = CommentForm(request.POST)
                if form.is_valid():
                    new = form.save(commit=False)
                    new.users = request.user
                    new.items = item
                    new.save()
                    return HttpResponseRedirect(f"{item.id}")
                else: 
                    # error
                    return render('auctions/item.html', {
                        'message': "",
                        'CommentForm': CommentForm(request.POST)
                    })
            else: 
                # error
                return HttpResponseRedirect(reverse("index"))
        else: 
            return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, 'auctions/item.html',{
            'item': item,
            'BidForm': BidForm(),
            'CommentForm': CommentForm(),
            'Comments': comments,
            'Bids': bids
        })

@login_required(login_url='/login')
def watchlist(request, item_id=None):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        form = Watchlist()
        form.items = item
        form.users = request.user
        form.save()
        return HttpResponseRedirect('/')
    else:
        watchlist = Watchlist.objects.filter(users=request.user)
        return render(request, 'auctions/watchlist.html', {
            'Watchlist': watchlist
        })

def filter(request, filter):
    if filter == "sold":
        pass
    else:
        pass