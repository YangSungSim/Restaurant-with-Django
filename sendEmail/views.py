from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.text import MIMENonMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

sys.path.append('D:/Django/RestaurantShare/')
from shareRes.models import *


# Create your views here.
def sendEmail(request):
    try:
        checked_res_list = request.POST.getlist('checks')
        inputReceiver = request.POST['inputReceiver']
        inputTitle = request.POST['inputTitle']
        inputContent = request.POST['inputContent']
        restaurants = []
        for checked_res_id in checked_res_list:
            restaurants.append( Restaurant.objects.get(id = checked_res_id))

        content = {'inputContent':inputContent,'restaurants':restaurants}

        msg_html = render_to_string('sendEmail/email_format.html',content)

        msg = EmailMessage(subject = inputTitle,body=msg_html,from_email='fpahsk98@gmail.com',bcc=inputReceiver.split(','))
        msg.content_subtype = 'html'

        msg.send()
        return render(request,'sendEmail/sendSuccess.html')
    except:
        return render(request,'sendEmail/sendFail.html')

