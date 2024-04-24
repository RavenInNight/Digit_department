from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):

    status = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]

    project = models.ForeignKey(
        Project,
        related_name='bug_report',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


