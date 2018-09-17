from django import forms

from .models import Attachment, Mail


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('attachment',)


class MailForm(forms.ModelForm):
    email_to = forms.CharField(required=True, widget=forms.TextInput(attrs={'data-role': 'tagsinput'}))
    email_cc = forms.CharField(required=True, widget=forms.TextInput(attrs={'data-role': 'tagsinput'}))

    class Meta:
        model = Mail
        fields = ('email_from', 'email_to', 'email_cc', 'subject', 'body')
