from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    email = models.EmailField(verbose_name='почта')
    message = models.TextField(verbose_name='сообщение')

    # message = models.TextField(verbose_name='сообщение', **NULLABLE)
    # message = models.TextField(verbose_name='сообщение', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.message}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
