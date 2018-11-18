""" Views for the application """
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.core.urlresolvers import reverse_lazy
from .forms import TaskForm

from helloworld.models import Task

import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(name)s %(levelname)s %(message)s',
)
class HomePageView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'index.html'

    def get_queryset(self):
        args = {'deleted': False}
        if self.kwargs.get('hidemarked', None):
            args['status'] = False
        return Task.objects.filter(**args)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hidemarked'] = self.kwargs.get('hidemarked', None)
        return context

class TaskNew(LoginRequiredMixin, CreateView):
    form_class = TaskForm 
    success_url = reverse_lazy('home')
    template_name = "task_new.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskNew, self).form_valid(form)


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('home')
    fields = ('name', 'description')
    template_name = 'task_edit.html'
    pk_url_kwarg = 'uuid'
    context_object_name = 'task'
    
    def get_object(self, *args, **kwargs):
        obj = super(TaskEdit, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    template_name = 'task_delete.html'
    pk_url_kwarg = 'uuid'
    context_object_name = 'task'
    
    def get_object(self, *args, **kwargs):
        obj = super(TaskDelete, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj

class TaskMark(LoginRequiredMixin, TemplateView):
    def get(self, request, uuid):
        task_to_mark = Task.objects.filter(uuid=uuid).first()
        if not task_to_mark:
            return HttpResponseNotFound()
        else:
            task_to_mark.done()
            return HttpResponseRedirect('/')

