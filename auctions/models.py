from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Articles(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_articles",default="")
	name=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	image=models.CharField(max_length=200)
	description=models.CharField(max_length=500)
	start_bid=models.DecimalField(decimal_places=2,max_digits=8)
	date=models.DateTimeField(default="")

class Bid(models.Model):
	Article=models.ForeignKey(Articles,on_delete=models.CASCADE,related_name="my_bids",default="")
	user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
	bid=models.DecimalField(decimal_places=2,max_digits=8)

class comments(models.Model):
	Article=models.ForeignKey(Articles,on_delete=models.CASCADE,related_name="my_comments",default="")
	user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
	comment=models.CharField(max_length=500)

class WatchList(models.Model):
	Article=models.ForeignKey(Articles,on_delete=models.CASCADE,default="")
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_watchlist",default="")

class Won(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_wins")
	lists=models.CharField(max_length=64)
	price=models.DecimalField(max_digits=8,decimal_places=2)
