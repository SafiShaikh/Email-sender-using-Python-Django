from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def email(request):
	return render(request, 'customer/email.html')


def email_info(request):
	myto      = request.POST['to']
	mysubject = request.POST['subject']
	mymessage = request.POST['message']

	# email
	send_mail(mysubject,mymessage,settings.EMAIL_HOST_USER,[myto], fail_silently=False)
	messages.success(request, 'Email Sent Successfully')
	return redirect('/customer/email/')

