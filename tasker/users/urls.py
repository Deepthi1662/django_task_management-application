# code django imports
from django.conf.urls import url
from django.contrib.auth import views as auth_views

# project level imports
from users.views import (
	UserCreationView, 
	UserDashBoardView,
	AdminDashboard,
	AdminAsignTask,
	AdminTaskList,
)

"""
         if django version 1.11 or less use app_name 
         if django version 2 remove app_name 
         app_name deprecated from django 2.0
"""

app_name = 'users'

urlpatterns = [

    url(r'^registration/$', UserCreationView.as_view(), name='registration'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/users/login/'}, name='logout'),
    url(r'^dashboard/$', UserDashBoardView.as_view(), name='dashboard'),
    url(r'^admin/$', AdminDashboard.as_view(), name='admindashboard'),
    url(r'^admin/taskslist/$', AdminTaskList.as_view(), name='admin_tasks'),
    url(r'^admin/asigntask/$', AdminAsignTask.as_view(), name='admin_asign_task'),
]