# Generated by Django 4.1.3 on 2022-11-19 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_student_student_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='course_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_rating',
            new_name='rating',
        ),
    ]
