# Generated by Django 4.1.7 on 2023-03-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='password',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]