# Generated by Django 4.2.6 on 2023-10-24 07:57

import FirstProject.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirstProject', '0002_resident_photo_alter_founder_year_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.BooleanField(blank=True, help_text='Живет в доме?', null=True, verbose_name='Дом')),
                ('flat', models.BooleanField(blank=True, help_text='Живет в квартире?', null=True, verbose_name='Квартира')),
                ('area', FirstProject.models.IntegerRangeField(help_text='Введите площадь жилья', verbose_name='Площадь')),
                ('address', models.CharField(blank=True, help_text='Укажите адрес жилья', max_length=100, verbose_name='Адрес')),
                ('cost', FirstProject.models.IntegerRangeField(help_text='Введите стоимость жилья', verbose_name='Стоимость')),
                ('resident', models.ForeignKey(help_text='Введите имя и фамилию жителя', on_delete=django.db.models.deletion.CASCADE, to='FirstProject.resident', verbose_name='Житель')),
            ],
            options={
                'db_table': 'Housing',
            },
        ),
    ]
