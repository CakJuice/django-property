# Generated by Django 2.1.1 on 2018-09-14 06:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='Key')),
                ('value', models.CharField(blank=True, max_length=200, null=True, verbose_name='Value')),
                ('created_by', models.ForeignKey(on_delete='RESTRICT', related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(on_delete='RESTRICT', related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=32, verbose_name='Activation Key')),
                ('expire', models.DateTimeField(verbose_name='Expire')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user_id', models.ForeignKey(on_delete='CASCADE', related_name='activations', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
