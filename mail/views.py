from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import MailForm


# Create your views here.
@login_required()
def mail_create(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
    else:
        form = MailForm(initial={'email_from': request.user.email})

    for field in form:
        print(field)
    return render(request, 'mail/mail_create.html', context={'form': form})
