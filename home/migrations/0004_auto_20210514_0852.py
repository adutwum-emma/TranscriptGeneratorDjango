# Generated by Django 3.1.5 on 2021-05-14 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_grade_the_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['Subject'], 'verbose_name_plural': 'Grades'},
        ),
        migrations.RemoveField(
            model_name='grade',
            name='total_score',
        ),
    ]