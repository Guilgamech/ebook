from django.conf import settings
from mailqueue.models import MailerMessage
from mailqueue.tasks import send_mail

from apps import user


def enviar_email_registro(usuario):
    subject = 'Bienvenido a nuestro sitio web'
    message = f'Hola {usuario.username}, gracias por registrarte en nuestro sitio web.'
    email_from = settings.EMAIL_HOST_USER
    user_new_email = usuario.email
    send = MailerMessage(subject=subject, content=message, from_address=email_from, to_address=user_new_email)
    send.save()
