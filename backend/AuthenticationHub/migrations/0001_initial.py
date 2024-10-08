# Generated by Django 4.2.10 on 2024-02-17 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='ProfileImages/')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='BannerImages/')),
                ('phone_code', models.BigIntegerField(blank=True, default=None, null=True)),
                ('phone_number', models.BigIntegerField(blank=True, default=None, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_recruiter', models.BooleanField(blank=True, default=False, null=True)),
                ('address_line1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_user_info',
            },
        ),
    ]
