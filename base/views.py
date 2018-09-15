from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignupForm


# @cache_page(settings.CACHE_TTL)
def homepage(request):
    return render(request, 'base/homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # UserActivation.send_user_activation(user)
            user = form.save()
            auth_login(request, user)
            return redirect('homepage')
    else:
        form = SignupForm()
    return render(request, 'base/signup.html', context={'form': form})


def signup_success(request):
    if 'email' not in request.GET:
        return redirect('homepage')
    return render(request, 'base/signup_success.html', context={'email': request.GET['email']})
