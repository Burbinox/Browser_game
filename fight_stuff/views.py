from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def show_user_stats(request):
    if request.user.is_authenticated:
        return render(request, 'user_stats.html')
    else:
        return redirect('/')
