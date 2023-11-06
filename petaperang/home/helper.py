from django.contrib import messages

from django.contrib.auth.models import User


from home.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token


def login(request):
    return User.objects.filter(user__username=request.POST.get('inputusername'),
                               user__password=hash(request.POST.get('inputpassword'))).exists()


def send_email(request):
    user = request.user
    mail_subject = 'Activate your user account.'
    message = render_to_string('message_text.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[request.user.email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{request.user.email}</b> inbox and click on \
               received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request,
                       f'Problem sending confirmation email to {request.user.email}, check if you typed it correctly.')
