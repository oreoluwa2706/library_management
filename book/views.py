from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.shortcuts import render

from rest_framework.decorators import api_view
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from templated_mail.mail import BaseEmailMessage

import book
from api.serializers import BookSerializer
from book.models import Book


def play_ground(request):
    send_mail('testing mail', 'this email is sent from django', '', ['cobaggrove@gmail.com'])
    return HttpResponse('email sent')


def playground(request):
    try:
        message = EmailMessage('testing mail', 'this email is sent from django', 'admin@gmail.com',
                               ['cobaggrove@gmail.com'])
        message.attach_file('book/static/images/foodoo.jpg')
        message.send()
    except BadHeaderError:
        pass
    return HttpResponse('email sentt')


def play_ground1(request):
    try:
        message = BaseEmailMessage(
            template_name='email/hello.html',
            context={'name': 'Asa'}
        )
        message.send(['asa@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse('email sent')
