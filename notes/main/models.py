from django.contrib.auth.models import User
from django.db import models


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notes', null=True)
    note = models.CharField(max_length=255, default=None, null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'
