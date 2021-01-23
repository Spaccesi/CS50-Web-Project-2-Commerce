from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	pass

''' 
Models:	Your application should have at least three models in addition to the User model: 
		-	one for auction listings, 
		-	one for bids, 
		-	and one for comments made on auction listings. 
		It’s up to you to decide what fields each model should have, and what the types of those fields should be. 
		You may have additional models if you would like.
'''

CATEGORIES = (
	('a', 'Electronics'),
    ('b', 'Sporting goods'),
    ('c', 'Home & Gardens'),
    ('d', 'Motor'),
    ('e', 'Fashion'),
    ('f', 'Other'),
)

class Category(models.Model):
	categories = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.categories}"


class Item(models.Model):
	"""Items listed on the site"""
	owners = models.ForeignKey(User, on_delete=models.PROTECT, related_name="owner")
	title = models.CharField(max_length=64)
	description = models.TextField()
	initial_bid = models.DecimalField(decimal_places=2, max_digits=19)
	# category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[5][1])
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	prices = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	bought = models.BooleanField(default=False)
	img = models.URLField(blank=True, null=True)

	def __str__(self):
		return f"{self.title} uploaded by {self.owners}" 

class Watchlist(models.Model):
	'''Watch list of Listed items of a User '''
	users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch_list_user")
	items = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)

class Comment(models.Model):
	"""Comment made by one User about one Listing Item"""
	users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_commented")

	def __str__(self):
		return f"{self.users} comment" 

class Bid(models.Model):
	"""Bid made by one User to one Listing Item"""
	users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user")
	bids = models.DecimalField(decimal_places=2, max_digits=19)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_bided")
	
	def __str__(self):
		return f"{self.users} made a {self.bids}" 

class Answer(models.Model):
	"""Responses of comments"""
	users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answer_user")
	content = models.TextField()
	comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="answer_comment")
