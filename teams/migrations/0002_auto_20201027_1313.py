# Generated by Django 3.1.1 on 2020-10-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.AddField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
