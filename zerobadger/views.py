from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(request, 'zerobadger/dashboard.html')
