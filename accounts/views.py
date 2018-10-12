from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from accounts.models import Token
from django.urls import reverse
from django.contrib import auth, messages
import sys
from django.conf import settings


# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        settings.EMAIL_HOST_USER,
        [email])
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in.")
    return redirect('/')


def login(request):
    print('login view', file=sys.stderr)
    uid = request.GET.get('token')
    user = auth.authenticate(uid)
    if user is not None:
        auth.login(request, user)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')
