# Generated by Django 4.1.3 on 2022-11-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_rename_course_name_courses_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
