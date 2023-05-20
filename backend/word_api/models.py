from django.db import models

from django.contrib.auth.models import User
from configure_api.models import Language



class Word(models.Model):
    word = models.CharField(max_length=255, blank=False, null=False)
    meaning = models.TextField(null=False, blank=False)
    base_language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False, related_name='base_language')
    translate_language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False, related_name='translate_language')
    is_deleted = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word