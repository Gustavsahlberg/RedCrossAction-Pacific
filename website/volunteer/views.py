from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.conf import settings

from .models import AddMail

def index(request):

    if request.method == 'POST':
        message = request.POST['message']

        recievers = []
        for mail in AddMail.objects.all():
            recievers.append(mail.mail_address)

        send_mail('Mail for help', message, settings.EMAIL_HOST_USER, recievers)

        # send_info2 = ('Mail for help',
        #     message, 
        #     settings.EMAIL_HOST_USER, 
        #     [reciever2], 
        #     )

        # datatuple = (
        #     ('Mail for Help', message, settings.EMAIL_HOST_USER, [reciever]),
        #     ('Mail for Order', message, settings.EMAIL_HOST_USER, [reciever2]),
        # )
        # send_mass_mail(datatuple)
        # send_mass_mail((send_info1, send_info2), fail_silently=False)

        
    latest_mail = AddMail.objects.order_by('-pub_date')[:5]
    context = {'latest_mail': latest_mail}
    return render(request, 'volunteer/index.html', context)
    