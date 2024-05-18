from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    created_at = models.DateTimeField(verbose_name='Fecha de creacion:', auto_now_add=True)
    start_date = models.DateTimeField(verbose_name='Fecha de inicio', default=timezone.now)
    overdue = models.DateTimeField(verbose_name='Fecha de vencimiento', null=True, blank=True)
    title = models.CharField(verbose_name='Titulo', max_length=100)
    content = models.TextField(verbose_name='Descripción', max_length=500)
    email = models.EmailField(verbose_name='Email',)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name='Task'
        verbose_name_plural='Tasks'

