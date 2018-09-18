import os
from time import time

from django.contrib.auth.models import User
from django.db import models
from django.core.mail import EmailMessage

from base.models import BaseModel


def rename_attachment(instance, filename: str):
    upload_to = 'mail_attachment/'
    ext = filename.split('.')[-1]
    new_path = '%s-%d.%s' % ('attachment', round(time() * 1000), ext,)
    return os.path.join(upload_to, new_path)


# Create your models here.
class Attachment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    attachment = models.FileField(upload_to=rename_attachment, max_length=200000, verbose_name="Attachment Path")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    created_by = models.ForeignKey(User, on_delete='RESTRICT', related_name='+', verbose_name="Created By")

    class Meta:
        ordering = ('created_at',)


class Mail(BaseModel):
    email_from = models.CharField(max_length=250, verbose_name="From")
    email_to = models.TextField(verbose_name="To")
    email_cc = models.TextField(verbose_name="CC", null=True, blank=True)
    subject = models.CharField(max_length=250, verbose_name="Subject")
    body = models.TextField(verbose_name="Body")
    attachment_ids = models.ManyToManyField(to=Attachment, related_name='mails')
    state = models.CharField(max_length=24, choices=(
        ('outgoing', "Outgoing"),
        ('sent', "Sent"),
        ('received', "Received"),
        ('exception', "Delivery Failed"),
        ('cancel', "Cancelled"),
    ), default='outgoing')
    send_at = models.DateTimeField(verbose_name="Send At", null=True, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ('created_at',)

    def send_mail(self):
        attachments = []
        for attach in self.attachment_ids:
            attachments.append(attach.attachment)

        try:
            email = EmailMessage(
                subject=self.subject,
                body=self.body,
                from_email=self.email_from,
                to=self.email_to.split(','),
                cc=self.email_cc.split(','),
                attachments=attachments,
            )
            email.content_subtype = 'html'
            email.send()
            self.state = 'sent'
        except Exception as e:
            self.state = 'exception'

        self.save()
