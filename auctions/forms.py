from django import forms
from .models import Item, Bid, Comment

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['title', 'description', 'initial_bid', 'category', 'img']
		labels = {
			'img': 'Image'
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'initial_bid': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 20%;'}),
			'category': forms.Select(attrs={'class': 'form-control'}),
			'img': forms.URLInput(attrs={'class': 'form-control'})
		}

class BidForm(forms.ModelForm):
	class Meta:
		model = Bid
		fields = ['bids']
		labels = {
			'bids' : ''
		}
		widgets = {
			'bids': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 20%;'})
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		labels = {
			'content' : ''
		}
		widgets = {
			'content' : forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 60px;'})
		}