from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout

def homeView(request):
    user = request.user
    print(user)
    if not user.is_authenticated:
        return redirect("login")
    todos = user.todos.all()
    context = {"todos": todos}
    return render(request, 'mvt/index.html', context=context)



def registerView(request):
    form = forms.CreateUserForm()

    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request=request, user=user)
                return redirect("home")
    context = {'register_form': form}
    return render(request, 'mvt/register.html', context=context)


def loginView(request):
    form = forms.LoginForm()

    if request.method == "POST":
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect("home")
    
    context = {'login_form': form}

    return render(request, "mvt/login.html", context=context)