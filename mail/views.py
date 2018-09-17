from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import JsonResponse

from .forms import MailForm, AttachmentForm


# Create your views here.
@login_required
def mail_create(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
    else:
        form = MailForm(initial={'email_from': request.user.email})
    return render(request, 'mail/mail_create.html', context={'form': form})


@login_required
def attachment_create(request):
    if request.method == 'POST' and request.is_ajax():
        form = AttachmentForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()
            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 0})
    return JsonResponse({})
