from django import forms
from .models import Laptop,Phone


class LaptopForm(forms.ModelForm):
	class Meta:
		model=Laptop
		fields=('name','price','status')


class PhoneForm(forms.ModelForm):
	class Meta:
		model=Phone
		fields=('name','price','status')