from django.conf.urls import *
from django.views.generic import UpdateView
from task.views import TaskUpdateView


app_name = 'task'
urlpatterns =[

	 url(r'^dotask/(?P<pk>\d+)$', TaskUpdateView.as_view(), name='new_task'),

]
