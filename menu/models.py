from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    parent = models.ForeignKey('self', **NULLABLE, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=100, **NULLABLE, verbose_name='URL')
    named_url = models.CharField(max_length=100, **NULLABLE, verbose_name='наименование URL')
    menu_name = models.CharField(max_length=50, verbose_name='наименование меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'
        ordering = ('pk',)
