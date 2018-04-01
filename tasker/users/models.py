from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
# Create your models here.


class TaskUser(AbstractUser):

    """
    extending AbstractUser Model for adding custom fields
    """

    confirm_details = models.BooleanField(default=False)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    #def get_absolute_url(self):
		#return reverse('users:user_details', args=[str(self.id)])