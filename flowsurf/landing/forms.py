from django import forms
from flowsurf.landing.models import Subscriber

class SubscriberForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		fields = ['name', 'email', 'phone', 'message']