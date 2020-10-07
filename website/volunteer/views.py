from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):

    if request.method == 'POST':
        message = request.POST['message']
        reciever = request.POST['reciever']


        send_mail('Mail for help',
            message, 
            settings.EMAIL_HOST_USER, 
            [reciever], 
            fail_silently=False)
    return render(request, 'volunteer/index.html')
    