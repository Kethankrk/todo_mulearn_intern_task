from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.db.models import F

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
    if not user.is_authenticated:
        return redirect("login")
    todos = user.todos.filter(completed=True)
    context = {'todos': todos}
    return render(request, 'mvt/todolog.html', context=context)

def todoUpdateView(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        todo = get_object_or_404(models.Todo, pk=todo_id)
        form = forms.TodoForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    todo_id = request.GET.get("id", None)
    if todo_id is None:
        return redirect("home")
    
    todo = models.Todo.objects.get(id=todo_id)
    if todo.user != request.user:
        return redirect("home")
    
    context = {"todo": todo, "expire": str(todo.expire.astimezone()).split("+")[0]}


    return render(request, 'mvt/updateTodo.html', context=context)



def profileView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    todos = user.todos.all()
    total_todo = todos.count()
    completed_todo = todos.filter(completed=True).count()
    expired_todo = todos.filter(expire__lt=timezone.now()).count()
    pending_todo = todos.filter(completed=False, expire__gt=timezone.now()).count()
    context = {"total": total_todo, "user": user, "completed": completed_todo, "expired": expired_todo, "pending": pending_todo}
    return render(request, 'mvt/profile.html', context=context)