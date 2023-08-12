from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is not None:
            login(request, user)
            return redirect('/bulimlar/')
        return redirect('/')

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def bulimlar(request):
    if request.user.is_authenticated:
        return render(request, 'bulimlar.html')
    return redirect(login)