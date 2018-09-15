from django import forms

from .models import Mail


class MailForm(forms.ModelForm):
    email_to = forms.CharField(required=True, widget=forms.TextInput(attrs={'data-role': 'tagsinput'}))
    email_cc = forms.CharField(required=True, widget=forms.TextInput(attrs={'data-role': 'tagsinput'}))

    class Meta:
        model = Mail
        fields = ('email_from', 'email_to', 'email_cc', 'subject', 'body', 'attachment', 'state', 'send_at')
