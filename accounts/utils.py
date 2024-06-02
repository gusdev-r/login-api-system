import random

from django.conf import settings
from django.core.mail import EmailMessage
from .models import User, OneTimePassword


def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(1, 9))
    return otp


def send_code_to_user(email):
    default_subject = "One time passcode for E-mail verification"
    otp_code = generate_otp()
    print(otp_code)
    user = User.objects.get(email=email)
    current_site = "myAuth.com"
    email_body = f"Hi {user.first_name} thanks for signing up on {current_site}, please verify your email with the \n on time passcode {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)
    send_email=EmailMessage(subject=default_subject, body=email_body, from_email=from_email, to=[email])
    send_email.send(fail_silently=True)