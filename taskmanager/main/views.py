from django.shortcuts import render, redirect

from .forms import CreateTaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, "main/index.html", {"title": "Главная страница",
                                               "tasks": tasks})


def about(request):
    return render(request, "main/about.html")


def create_task(request):
    error = ""
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма заполнена не корректно"

    form = CreateTaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, "main/create_task.html", context)
