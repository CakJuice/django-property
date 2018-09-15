from django import forms

from .models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('email_from', 'email_to', 'email_cc', 'subject', 'body', 'attachment', 'state', 'send_at')
