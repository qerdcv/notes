from django.db import models


class Notes(models.Model):
    user = models.CharField(max_length=255, default=None, null=True, blank=True)
    note = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.user
