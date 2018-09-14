from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel


# Create your models here.
class Mail(BaseModel):
    user_id = models.ForeignKey(User, on_delete='CASCADE', related_name='mails', verbose_name='User')
    email_from = models.CharField(max_length=250, verbose_name="From")
    email_to = models.TextField(verbose_name="To")
    email_cc = models.TextField(verbose_name="CC")
    subject = models.CharField(max_length=250, verbose_name="Subject")
    body = models.TextField(verbose_name="Body")
    attachment = models.TextField(verbose_name="Attachment")
    state = models.CharField(max_length=24, choices=(
        ('outgoing', "Outgoing"),
        ('sent', "Sent"),
        ('received', "Received"),
        ('exception', "Delivery Failed"),
        ('cancel', "Cancelled"),
    ))
    send_at = models.DateTimeField(verbose_name="Send At", null=True, blank=True)

    def __str__(self):
        return self.subject
