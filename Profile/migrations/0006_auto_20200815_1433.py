# Generated by Django 3.0.6 on 2020-08-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20200809_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='citizenship_Status',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
