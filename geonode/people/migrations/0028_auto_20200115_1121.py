# Generated by Django 2.2.9 on 2020-01-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0027_auto_20200114_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]