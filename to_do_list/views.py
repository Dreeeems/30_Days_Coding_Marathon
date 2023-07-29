from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todos
from .forms import TodosForm
# Create your views here.

def index(request):
    return render(request,'todo/index.html',{
        'todos': Todos.objects.all()
    })



from django.shortcuts import render, redirect,get_object_or_404
from .forms import TodosForm
from .models import Todos

def add(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            new_todo_name = form.cleaned_data['todo_name']
            new_todo_desc = form.cleaned_data['todo_desc']
            new_todo_status = form.cleaned_data['todo_status']

            new_todo = Todos(
                todo_name=new_todo_name,
                todo_desc=new_todo_desc,
                todo_status=new_todo_status  # Corrected the field name here
            )
            new_todo.save()

            return render(request, 'todo/add.html', {
                'form': TodosForm(),
                'success': True
            })
    else:
        form = TodosForm()
    return render(request, 'todo/add.html', {
        'form': form
    })


def edit(request, id):
    todo = get_object_or_404(Todos, pk=id)

    if request.method == 'POST':
        form = TodosForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return render(request, 'todo/edit.html', {
                "form": form,
                'success': True
            })
    else:
        form = TodosForm(instance=todo)

    return render(request, 'todo/edit.html', {
        'form': form
    })



def delete(request, id):
    todo = get_object_or_404(Todos, pk=id)

    if request.method == 'POST':
       todo.delete()
        
  

    return HttpResponseRedirect(reverse('index'))