# Generated by Django 3.1.3 on 2020-12-02 04:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='discard_Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('course_Attended', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_Picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('employee_ID', models.CharField(default='S123456D', max_length=15)),
                ('nric', models.CharField(max_length=20, null=True)),
                ('typeOfEmployee', models.CharField(choices=[('DIRECT', 'DIRECT'), ('INDIRECT', 'INDIRECT')], default='DIRECT', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=6)),
                ('address_1', models.CharField(max_length=250, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=250, verbose_name='address2')),
                ('date_Of_Passport_Expiry', models.DateField(blank=True, null=True)),
                ('citizenship_Status', models.CharField(default='-', max_length=100)),
                ('date_Of_Hire', models.DateField()),
                ('job_Title', models.CharField(max_length=100)),
                ('employment_Type', models.CharField(choices=[('Contractor', 'CONTRACTOR'), ('Full-time', 'FULL-TIME'), ('Part-time', 'PART-TIME'), ('Internship', 'INTERN')], default='Full-time', max_length=30)),
                ('skill1', models.CharField(blank=True, max_length=50, null=True)),
                ('skill2', models.CharField(blank=True, max_length=50, null=True)),
                ('skill3', models.CharField(blank=True, max_length=50, null=True)),
                ('second_Reporting_Manager', models.CharField(blank=True, max_length=200, null=True)),
                ('division_Centre', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.departments')),
                ('first_Reporting_Manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(max_length=150)),
                ('graduation_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1920), django.core.validators.MaxValueValidator(2200)])),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
        migrations.AddField(
            model_name='departments',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
    ]
