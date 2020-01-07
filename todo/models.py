from django.db import models


class Todo(models.Model):
    DONE_CHOICES = (
        (False, 'NOT DONE'),
        (True, 'DONE')
    )
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=True, choices=DONE_CHOICES)

    class Meta:
        ordering = ['-created_at']