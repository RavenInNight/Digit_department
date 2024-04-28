from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):

    STATUS_CHOICES = [
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

    # новое поле статуса задачи
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):

    STATUS_CHOICES = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Denied', 'Отклонено'),
    ]

    project = models.ForeignKey(
        Project,
        related_name='feature_request',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True
    )

    # новое поле статуса задачи
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
