# Generated by Django 4.1.3 on 2022-11-09 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_studentregistration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentregistration',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='studentregistration',
            name='lname',
        ),
    ]
