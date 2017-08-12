from django import forms
from .models import *

class SubsForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		"""docstring for ClassName"""
		model = Subscr
		exclude = []