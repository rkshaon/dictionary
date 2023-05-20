from django.db import models

from django.contrib.auth.models import User



class Language(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name