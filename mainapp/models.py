from django.db import models


# Create your models here.


class Comment(models.Model):
    text = models.CharField(max_length=150, verbose_name='Комментарий')
    start_time = models.IntegerField(null=True, blank=True, verbose_name='C: ')
    finish_time = models.IntegerField(null=True, blank=True, verbose_name='До: ')


class Point(models.Model):
    time = models.IntegerField(verbose_name='Время')
    val = models.FloatField(verbose_name='Значение')
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Комментарий')
    more_time = models.IntegerField(verbose_name='Верхний допуск по времени')
    less_time = models.IntegerField(verbose_name='Нижний допуск по времени')
    more_value = models.IntegerField(verbose_name='Верхний допуск по значению')
    less_value = models.IntegerField(verbose_name='Нижний допуск по значению')

    def __str__(self):
        return f'Time: {self.time} Value: {self.val}'


class Interval(models.Model):
    val = models.IntegerField(verbose_name='Интервал')
    point_a = models.ForeignKey(Point, on_delete=models.CASCADE, verbose_name='Начальная точка', related_name='point_a')
    point_b = models.ForeignKey(Point, on_delete=models.CASCADE, verbose_name='Конечная точка', related_name='point_b')
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Комментарий')

