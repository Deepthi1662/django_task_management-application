from django import forms
from task.models import task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'