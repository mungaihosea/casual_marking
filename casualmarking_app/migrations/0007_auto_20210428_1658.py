# Generated by Django 3.2 on 2021-04-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casualmarking_app', '0006_alter_task_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='account_type',
            field=models.CharField(default='marker', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='account_type',
            field=models.CharField(default='student', max_length=20),
        ),
    ]
