from django.shortcuts import render, redirect
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import *

def index(request):

    if request.method == 'POST':
        message = request.POST['message']
        reciever = request.POST['reciever']
        
        q = Question(id=None, message=message)
        q.save()

        return redirect('mail/answer/?id=' + q.id)
    return render(request, 'volunteer/index.html')
    
def answer(request):
    try:
        id = int(request.GET['id'])

        q = Question.objects.get(id=id)

        if request.method == 'POST':
            c = request.POST['choice']
            
            if c == 'yes':
                c = True
            elif c == 'no':
                c = False
            else:
                return render_to_string('volunteer/answer.html', {'errorMessage': 'Invalid choice.', 'message': q.message}, request)

            Choice(id=None, choice=c, question=q).save()
        return render_to_string('volunteer/answer.html', {'message': q.message}, request)
    except ObjectDoesNotExist:
        return HttpResponse("The specified id is not valid.", "text/plain")
