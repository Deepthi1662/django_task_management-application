# core django imports
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# project level imports
from users.forms import TaskUserForm
from users.models import TaskUser

from task.models import Task
# Create your views here.


class UserCreationView(CreateView):
    form_class = TaskUserForm
    template_name = 'user_signup.html'

    """
        Overriding dispatch if user is authenticated he won't able to view signup view   
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('users:dashboard'))
        return super(UserCreationView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users:login')


class UserDashBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
    	if request.user.is_superuser:
    		return HttpResponseRedirect(reverse('users:admindashboard'))
    	return super(UserDashBoardView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(UserDashBoardView, self).get_context_data(**kwargs)
        context['new_tasks'] = Task.objects.filter(reporter=self.request.user).exclude(completed=True)
        context['completed_tasks'] = Task.objects.filter(reporter=self.request.user, completed=True)
        return context


class UserDetails(LoginRequiredMixin, TemplateView):
	model = TaskUser
	template_name = 'user_details.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_admin:
			return HttpResponseRedirect(reverse('users:admindashboard'))
		return super(UserDetails, self).dispatch(request, *args, **kwargs)


class AdminDashboard(LoginRequiredMixin, TemplateView):
    model = TaskUser
    template_name = 'admin_index.html'
    def get_context_data(self, **kwargs):
        context = super(AdminDashboard, self,).get_context_data(**kwargs)
        context['users'] = TaskUser.objects.all().exclude(username=self.request.user.username)
        context['tasks'] = Task.objects.all()
        context['total_tasks'] = Task.objects.all().count()
        context['total_users'] = TaskUser.objects.all().exclude(username=self.request.user.username).count()
        context['total_onetime_tasks'] = Task.objects.filter(task_type='ONE_TIME').count()
        context['total_repeat_tasks'] = Task.objects.filter(task_type='REPEAT').count()
        return context 


class AdminAsignTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'discription', 'task_type', 'reporter']
    template_name = 'admin_asign_task.html'
    success_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context = super(AdminAsignTask, self,).get_context_data(**kwargs)
        context['users'] = TaskUser.objects.all().exclude(username=self.request.user.username)
        context['tasks'] = Task.objects.all()
        context['total_tasks'] = Task.objects.all().count()
        context['total_users'] = TaskUser.objects.all().exclude(username=self.request.user.username).count()
        context['total_onetime_tasks'] = Task.objects.filter(task_type='ONE_TIME').count()
        context['total_repeat_tasks'] = Task.objects.filter(task_type='REPEAT').count()
        return context 

class AdminTaskList(LoginRequiredMixin, ListView):
    ogin_url = '/users/login/'
    model = Task
    queryset = Task.objects.all()
    template_name = 'admin_task_list.html'
    context_object_name = 'admin_tasks'