# Generated by Django 3.0.6 on 2020-09-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GnC', '0010_auto_20200915_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmental_goals',
            name='due',
            field=models.DateField(),
        ),
    ]
