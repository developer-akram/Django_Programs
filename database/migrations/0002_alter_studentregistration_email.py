# Generated by Django 4.1.3 on 2022-11-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
