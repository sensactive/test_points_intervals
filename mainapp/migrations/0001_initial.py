# Generated by Django 2.2.2 on 2019-06-28 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150, verbose_name='Комментарий')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='C: ')),
                ('finish_time', models.DateTimeField(blank=True, null=True, verbose_name='До: ')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(verbose_name='Время')),
                ('val', models.FloatField(verbose_name='Значение')),
                ('more_time', models.IntegerField(verbose_name='Верхний допуск по времени')),
                ('less_time', models.IntegerField(verbose_name='Нижний допуск по времени')),
                ('more_value', models.IntegerField(verbose_name='Верхний допуск по значению')),
                ('less_value', models.IntegerField(verbose_name='Нижний допуск по значению')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Comment', verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.IntegerField(verbose_name='Интервал')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Comment', verbose_name='Комментарий')),
                ('point_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_a', to='mainapp.Point', verbose_name='Начальная точка')),
                ('point_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_b', to='mainapp.Point', verbose_name='Конечная точка')),
            ],
        ),
    ]