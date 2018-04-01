from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from task.models import Task
# Create your views here.



class TaskUpdateView(UpdateView):
	model = Task
	template_name = 'task_update.html'
	fields = ['name','discription','image', 'video', 'completed', 'progress']
	success_url = reverse_lazy('users:dashboard')
