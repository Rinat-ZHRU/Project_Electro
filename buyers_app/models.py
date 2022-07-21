from django.db import models


class Buyer(models.Model):  # покупатели
    """Покупатели"""
    full_name = models.CharField('Полное имя покупателя(ФИО)', max_length=100)
    email = models.EmailField('Электронная почта')
    telephone = models.CharField('Телефоны', max_length=20)
    consent = models.BooleanField('Согласие на обработку персональных данных', default=False)


    class Meta:
        ordering = ['full_name']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f'{self.full_name}, {self.telephone}'

