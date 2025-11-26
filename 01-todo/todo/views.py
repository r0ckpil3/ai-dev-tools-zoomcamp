from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

from .models import Todo
from .forms import TodoForm

class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"

class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/todo_detail.html"
    context_object_name = "todo"

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:list")

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy("todo:list")


@require_POST
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    # Toggle using POST form value 'completed' if present, otherwise flip
    if 'completed' in request.POST:
        todo.completed = request.POST.get('completed') in ['true', '1', 'on', 'checked']
    else:
        todo.completed = not todo.completed
    todo.save()
    return redirect(request.META.get('HTTP_REFERER', reverse_lazy('todo:list')))

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo:list")