from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User,Articles,Bid,comments,WatchList,Won
import datetime


def index(request):

    return render(request, "auctions/index.html",{
        "content":Articles.objects.all()
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

def article_register(request):
    return render(request,"auctions/articles.html")

def Items(request):
    if request.method=="POST":
        name=request.POST["name"]
        category=request.POST["Category"]
        image=request.POST["image"]
        description=request.POST["description"]
        start_bid=request.POST["start_bid"]
        user=request.user
        date=datetime.datetime.now()
        check=Articles.objects.filter(name=name).first()
        if check is not None:
            return HttpResponse("please change the Article name")
        instance=Articles(user=user,name=name,category=category,image=image,description=description,start_bid=start_bid,date=date)
        instance.save()
        bid_input=Bid(Article=instance,user=instance.user,bid=instance.start_bid)
        bid_input.save()
        return HttpResponseRedirect(reverse("index"))

def category_page(request):
    return render(request,"auctions/category.html")

def category(request,link):
    types=Articles.objects.filter(category=link)
    return render(request,"auctions/display.html",{
        "type":types
        })

@login_required(login_url='/login')
def details(request,type):
    det=Articles.objects.get(name=type)
    com=det.my_comments.all()
    current=det.my_bids.last()
    return render(request,"auctions/links.html",{
        "detail":det,"current":current,"com":com
        })    

def place_bid(request,type):
    bid_input=float(request.POST["bid_placed"])
    user=request.user
    item=Articles.objects.get(name=type)
    last_bid=item.my_bids.last()
    if bid_input<=last_bid.bid:
        return HttpResponse("your bid should be greater than current bid")
    new_bid=Bid(Article=item,user=request.user,bid=bid_input)
    new_bid.save()
    return HttpResponseRedirect(reverse("index"))

def review(request,type):
    user=request.user
    item=Articles.objects.get(name=type)
    review=request.POST["review"]
    instance=comments(user=user,Article=item,comment=review)
    instance.save()
    return HttpResponseRedirect(reverse("details",args=[type]))

def watchlist(request):
    username=request.user
    list=username.my_watchlist.all()
    return render(request,"auctions/watchlist.html",{
        "items":list
        })
def add_watch(request,type):
    user=request.user
    item=Articles.objects.get(name=type)
    check=user.my_watchlist.all()
    for i in check:
        if type==i.Article.name:
            return HttpResponse("Already in WatchList")
    instance=WatchList(user=user,Article=item)
    instance.save()
    return HttpResponseRedirect(reverse("watchlist"))

def remove(request,type):
    item=Articles.objects.get(name=type)
    WatchList.objects.filter(user=request.user).filter(Article=item).delete()
    return HttpResponseRedirect(reverse("watchlist"))

def close_bid(request,watchitem):
    list_item=Articles.objects.get(name=watchitem)
    current=list_item.my_bids.last().bid
    username=list_item.my_bids.last().user
    instance=Won(user=username,lists=watchitem,price=current)
    instance.save()
    list_item.delete()
    return render(request,"auctions/declare.html",{
        "user":username,"price":current,"watchitem":watchitem
        })
def won(request):
    username=request.user
    mylist=username.my_wins.all()
    context={"mylist":mylist}
    return render(request,"auctions/result_user.html",context)