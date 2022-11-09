# Generated by Django 4.1.3 on 2022-11-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('states', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('courses', models.CharField(max_length=50)),
                ('txtarea', models.CharField(max_length=50)),
            ],
        ),
    ]
