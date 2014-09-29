from django.shortcuts import render
from .forms import SubscriberForm
from django_ajax.decorators import ajax


@ajax
def ajax_landing(request):
	form = SubscriberForm(request.POST)
	if form.is_valid():
		form.save()
		return {'text': "<div class='content-message'> <i class='fa fa-rocket fa-3x'></i> <h2>Email Sent Successfully</h2> <p>Your message has been submitted.</p> </div>"}
	else:
		print form.errors
		return {'text': 'asdasdasd'}

def landing(request):
	if request.POST:
		form = SubscriberForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			print form.errors
	return render(request, 'landing.html')
