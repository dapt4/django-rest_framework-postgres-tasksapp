# Generated by Django 4.0.6 on 2022-07-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
