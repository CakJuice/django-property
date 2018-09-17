# Generated by Django 2.1.1 on 2018-09-17 03:40

from django.conf import settings
from django.db import migrations, models
import mail.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(max_length=200000, upload_to=mail.models.rename_attachment)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete='RESTRICT', related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('email_from', models.CharField(max_length=250, verbose_name='From')),
                ('email_to', models.TextField(verbose_name='To')),
                ('email_cc', models.TextField(blank=True, null=True, verbose_name='CC')),
                ('subject', models.CharField(max_length=250, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('state', models.CharField(choices=[('outgoing', 'Outgoing'), ('sent', 'Sent'), ('received', 'Received'), ('exception', 'Delivery Failed'), ('cancel', 'Cancelled')], default='outgoing', max_length=24)),
                ('send_at', models.DateTimeField(blank=True, null=True, verbose_name='Send At')),
                ('attachment_ids', models.ManyToManyField(related_name='mails', to='mail.Attachment')),
                ('created_by', models.ForeignKey(on_delete='RESTRICT', related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(on_delete='RESTRICT', related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]