# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from .forms import RegistrationForm
from django.contrib.auth import login


def sign_up(request):
    if request.method == "POST":
        # save user
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/items')
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {'form': form})