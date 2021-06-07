# Generated by Django 3.1.5 on 2021-05-11 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_class', models.CharField(max_length=200)),
                ('class_code', models.CharField(max_length=200, unique=True)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Classes',
                'ordering': ['name_of_class'],
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_score', models.FloatField(blank=True, null=True)),
                ('exam_score', models.FloatField(blank=True, null=True)),
                ('total_score', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='SchoolLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='school_logos')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('parent_phone', models.CharField(max_length=100)),
                ('prarent_email', models.CharField(blank=True, max_length=200, null=True)),
                ('passport_pic', models.ImageField(upload_to='profile_photos')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.class')),
            ],
            options={
                'verbose_name_plural': 'Students',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=100)),
                ('student', models.ManyToManyField(through='home.Grade', to='home.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.AddField(
            model_name='grade',
            name='Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student'),
        ),
    ]