from django.shortcuts import render, redirect
from django.urls import reverse
from api.forms import RegistrationForm
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'api/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('api:login'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'api/reg_form.html', args)
