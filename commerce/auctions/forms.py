from django import forms
from .models import ListingModel

class ListingForm(forms.ModelForm):
	class Meta:
		model = ListingModel
		fields = ['title', 'description', 'img', 'initial_bid']
		
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'img': forms.FileInput(attrs={'class': 'form-control-file'}),
			'initial_bid': forms.NumberInput(attrs={'class': 'form-control'})
		}
