from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from fight_stuff.models import Stats


def index(request):
    if request.method == 'POST':
        login = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=login, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/')
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password_conf = request.POST['password_conf']

            if password == password_conf:
                if User.objects.filter(username=login).exists():
                    messages.info(request, "username taken")
                    return render(request, 'register.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email taken")
                    return render(request, 'register.html')
                else:
                    user = User.objects.create_user(username=login, password=password, email=email)
                    user_stats = Stats.objects.create(user=user, endurance=100, resistance=10, strength=10, speed=10,
                                                      agility=10, mind_power=10)
                    user_stats.save()
                    user.save()
                    return redirect('/')
            else:
                messages.info(request, "passwords not match")
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    else:
        return redirect('/')


def show_all_object_from_db(request):
    all_users = User.objects.all()
    print(all_users)
    for user in all_users:
        print(user.username)
        print(user.email)
        print(user.stats.endurance)
    return redirect('/')
