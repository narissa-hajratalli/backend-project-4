# Generated by Django 3.1.1 on 2020-09-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat_consumption', '0013_auto_20200920_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyconsumption',
            name='day_consumed',
            field=models.DateField(verbose_name='2020-09-14'),
        ),
    ]
