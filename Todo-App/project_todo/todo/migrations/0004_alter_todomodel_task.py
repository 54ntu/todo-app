# Generated by Django 5.0.7 on 2024-07-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todomodel_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='task',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
