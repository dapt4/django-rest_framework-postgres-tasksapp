# Generated by Django 4.0.6 on 2022-07-04 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(verbose_name=datetime.date(2022, 7, 4)),
        ),
    ]
