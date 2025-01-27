# Generated by Django 4.2.6 on 2023-10-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='residents/%Y/%m/%D'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='year_of_birth',
            field=models.DateField(help_text='Введите дату рождения основателя', verbose_name='Дата рождения'),
        ),
    ]
