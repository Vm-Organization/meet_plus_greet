from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from mpg.settings import SITE_URL, DEFAULT_FROM_EMAIL
from .models import Booking


@receiver(post_save, sender=Booking)
def get_respond(sender, instance, created, **kwargs):
    # we will send message to admin and to customer

    # TODO: check updating booking status
    if not created:
        destination = [instance.email, DEFAULT_FROM_EMAIL]
        title = 'Бронирование'
        text = f"""Аэропорт отправления: {instance.departure_airport}\n
                Аэропорт прибытия: {instance.arrival_airport}\n
                Дата вылета: {instance.departure_datetime}\n
                Дата прибытия: {instance.arrival_datetime}\n
                Количество человек: {instance.passenger_number}\n
                Стоимость: {instance.get_total_price()}\n
                Статус: {instance.booking_status}\n
                Дополнительная информация: {instance.additional_info}\n
                Email: {instance.email}\n
                Телефон: {instance.phone}\n
                Телеграм: {instance.telegram}\n
                """

        send_notification_about_respond(instance, title, text, destination)


def send_notification_about_respond(instance, title, text, destination):
    html_content = render_to_string(
        'account/email.html',
        {
            'title': title,
            'text': text,
            'link': f'{SITE_URL}/booking/{instance.id}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        from_email=DEFAULT_FROM_EMAIL,
        to=destination
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

