# Generated by Django 5.0.6 on 2024-08-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserprofileStation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
