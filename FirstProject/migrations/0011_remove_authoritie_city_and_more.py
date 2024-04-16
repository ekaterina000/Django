# Generated by Django 4.2.6 on 2023-12-11 15:49

import FirstProject.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirstProject', '0010_alter_district_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authoritie',
            name='city',
        ),
        migrations.RemoveField(
            model_name='citie',
            name='date_of_foundation',
        ),
        migrations.RemoveField(
            model_name='citie',
            name='founder',
        ),
        migrations.RemoveField(
            model_name='citie',
            name='population',
        ),
        migrations.RemoveField(
            model_name='citie',
            name='power_id',
        ),
        migrations.RemoveField(
            model_name='countrie',
            name='area',
        ),
        migrations.RemoveField(
            model_name='countrie',
            name='language',
        ),
        migrations.RemoveField(
            model_name='district',
            name='authoritie',
        ),
        migrations.RemoveField(
            model_name='district',
            name='city',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='house',
        ),
        migrations.RemoveField(
            model_name='resident',
            name='city',
        ),
        migrations.AddField(
            model_name='authoritie',
            name='country',
            field=models.ForeignKey(blank=True, help_text='Выберите страну представителя власти', null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstProject.countrie', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='citie',
            name='districts',
            field=models.ManyToManyField(to='FirstProject.district'),
        ),
        migrations.AddField(
            model_name='citie',
            name='government',
            field=models.ForeignKey(blank=True, help_text='Выберите представителя власти', null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstProject.authoritie', verbose_name='Власть'),
        ),
        migrations.AddField(
            model_name='district',
            name='population',
            field=FirstProject.models.IntegerRangeField(blank=True, help_text='Введите численность района', null=True, verbose_name='Численность населения района'),
        ),
        migrations.AddField(
            model_name='housing',
            name='city',
            field=models.ForeignKey(blank=True, help_text='Введите название города', null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstProject.citie', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='resident',
            name='district',
            field=models.ForeignKey(blank=True, help_text='Введите район города', null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstProject.district', verbose_name='Район города'),
        ),
        migrations.AlterField(
            model_name='citie',
            name='country',
            field=models.ForeignKey(blank=True, help_text='Введите название страны, в которой находится этот город', null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstProject.countrie', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='citie',
            name='name',
            field=models.CharField(blank=True, help_text='Введите название города', max_length=100, primary_key=True, serialize=False, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='countrie',
            name='capital',
            field=models.CharField(blank=True, help_text='Введите столицу этой страны', max_length=50, null=True, verbose_name='Столица'),
        ),
        migrations.AlterField(
            model_name='countrie',
            name='name',
            field=models.CharField(blank=True, help_text='Введите название страны', max_length=100, primary_key=True, serialize=False, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(blank=True, help_text='Введите район города', max_length=100, primary_key=True, serialize=False, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='address',
            field=models.CharField(blank=True, help_text='Укажите адрес жилья', max_length=100, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='area',
            field=FirstProject.models.IntegerRangeField(blank=True, help_text='Введите площадь жилья', null=True, verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='cost',
            field=FirstProject.models.IntegerRangeField(blank=True, help_text='Введите стоимость жилья', null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='resident',
            field=models.ForeignKey(blank=True, help_text='Введите имя и фамилию жителя', null=True, on_delete=django.db.models.deletion.CASCADE, to='FirstProject.resident', verbose_name='Житель'),
        ),
        migrations.DeleteModel(
            name='Founder',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
