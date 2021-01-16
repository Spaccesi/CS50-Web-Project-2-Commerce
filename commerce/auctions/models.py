from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	pass

''' 
	Your application should have at least three models in addition to the User model: 
		one for auction listings, 
		one for bids, 
		and one for comments made on auction listings. 
	It’s up to you to decide what fields each model should have, and what the types of those fields should be. 
	You may have additional models if you would like.
'''

class BidModel(models.Model):
	"""Bid made by one User to one Listing Item"""
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	bid = models.DecimalField(decimal_places=2, max_digits=19)


class CommentModel(models.Model):
	"""Comment made by one User about one Listing Item"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()


class ListingModel(models.Model):
	"""Items listed on the site"""
	owner = models.ForeignKey(User, on_delete=models.PROTECT)
	title = models.CharField(max_length=64)
	description = models.TextField()
	img = models.ImageField()
	initial_bid = models.DecimalField(decimal_places=2, max_digits=19)
	comments = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
	last_bid = models.ForeignKey(BidModel, on_delete=models.CASCADE)
	created_on = models.DateField()		
		