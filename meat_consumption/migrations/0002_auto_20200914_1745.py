# Generated by Django 3.1.1 on 2020-09-14 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat_consumption', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyconsumption',
            old_name='days_consumed_this_week',
            new_name='weekly_total_consumption',
        ),
    ]