# Generated by Django 3.1.1 on 2020-09-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat_consumption', '0007_remove_dailyconsumption_day_consumed'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyconsumption',
            name='day_consumed',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailyconsumption',
            name='consumed',
            field=models.CharField(max_length=3),
        ),
    ]
