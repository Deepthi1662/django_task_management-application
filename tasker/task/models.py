from django.db import models
from users.models import TaskUser
# Create your models here.


class Task(models.Model):
	TYPES = (
		('ONE_TIME', 'ONE_TIME'),
		('REPEAT', 'REPEACT'),
	)
	name = models.CharField(max_length=100)
	discription = models.TextField()
	reporter = models.ForeignKey(TaskUser, on_delete=models.CASCADE)
	task_type = models.CharField(max_length=15, choices=TYPES)
	completed = models.BooleanField(default=False)
	image = models.FileField(upload_to="hotels/", blank=True)
	video = models.FileField(upload_to='hotels/', blank=True)
	progress = models.IntegerField(default=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	