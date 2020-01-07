from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin


class DoneListView(ListView):
    model = Todo
    context_object_name = 'done_list'
    template_name = 'todo/todo_done.html'


class NotDoneListView(ListView):
    model = Todo
    context_object_name = 'notdone_list'
    template_name = 'todo/todo_not_done.html'


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'todo/todo_list.html'
    paginate_by = 5


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('list')
    template_name = 'todo/todo_create_form.html'

    login_url = '/login'


class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'todo'


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['content', 'done']
    template_name = 'todo/todo_update_form.html'

    login_url = '/login'

    def get_success_url(self):
        todo_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={'pk': todo_pk})
        return url


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('list')

    login_url = '/login'