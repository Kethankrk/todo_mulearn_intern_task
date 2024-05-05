from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

def homeView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    form = forms.TodoForm()
    if request.method == "POST":
        form = forms.TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
    todos = user.todos.filter(completed=False)
    context = {"todos": todos, "form": form}
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

def logoutView(request):
    logout(request)
    return redirect('login')

def deleteTodoView(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        todo = models.Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect("home")
    return redirect("home")


def markTodoDoneView(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        todo = models.Todo.objects.get(id=todo_id)
        todo.completed = True
        todo.completed_at = timezone.now()
        todo.save()
        return redirect("home")
    return redirect("home")

def todoLogView(request):
    user = request.user

    todos = user.todos.filter(completed=True)
    context = {'todos': todos}
    return render(request, 'mvt/todolog.html', context=context)