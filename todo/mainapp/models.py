from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    done = models.BooleanField(default=False, verbose_name='выполнено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    deadline = models.DateField(verbose_name='дедлайн')
    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задача'
        ordering = ['-deadline']