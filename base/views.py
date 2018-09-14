from django.shortcuts import render, redirect

from .forms import SignupForm
from .models import UserActivation


# @cache_page(settings.CACHE_TTL)
def homepage(request):
    return render(request, 'base/homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            UserActivation.send_user_activation(user)
    else:
        form = SignupForm()
    return render(request, 'base/signup.html', context={'form': form})


def signup_success(request):
    if 'email' not in request.GET:
        return redirect('homepage')
    return render(request, 'base/signup_success.html', context={'email': request.GET['email']})
