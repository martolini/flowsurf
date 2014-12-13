from django import forms
from flowsurf.landing.models import Subscriber
from django.core.mail import send_mail


class SubscriberForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		fields = ['name', 'email', 'phone', 'message']

	def save(self, *args, **kwargs):
		super(SubscriberForm, self).__init__(*args, **kwargs)
		send_mail('New message from flowsurf.co',
			"Name: %s\nEmail: %s\nPhone: %s\n%s" % (self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['phone'], self.cleaned_data['message']),
			'kjetil@flow.surf',
			['kjetil@flow.surf'],
		)