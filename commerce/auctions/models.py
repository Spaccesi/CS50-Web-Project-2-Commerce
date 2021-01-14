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

class ListingItem(models.Model):
	owner = models.ForeignKey('User', on_delete=models.CASCADE)
	title = models.CharField(max_lenght=120)
	description = models.TextField()
	image = models.ImageField()
	date = models.DateTimeField()
	# category = 

	def date(self):
        return self.date.strftime('%B %d %Y')

class Bid(models.Model):
	user = models.ForeignKey('User', on_delete=models.PROTECT)
	item = models.ForeignKey('ListingItem', on_delete=models.CASCADE)
	bid = models.FloatField(decimal_places=2)
	date = models.DateTimeField()
	
	def __str__(self):
		return f"{self.bid}€"

class Comment(models.Model):
	user = models.ForeignKey('User')
	content = models.CharField()
	date = models.DateTimeField()
	item = models.ForeignKey('ListingItem')