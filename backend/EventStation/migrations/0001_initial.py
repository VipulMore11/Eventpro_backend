# Generated by Django 5.0.6 on 2024-08-03 19:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserprofileStation', '0001_initial'),
        ('VenueStation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('location', models.CharField(default='', max_length=30)),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_by_mentor', models.BooleanField(default=False)),
                ('approved_by_hod', models.BooleanField(default=False)),
                ('approved_by_dean', models.BooleanField(default=False)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='event/banner/')),
                ('associate', models.ManyToManyField(blank=True, to='UserprofileStation.userprofile')),
                ('committee', models.ManyToManyField(blank=True, to='UserprofileStation.committee')),
                ('venue', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='VenueStation.venue')),
            ],
            options={
                'db_table': 'eventStation_eventDetails',
            },
        ),
        migrations.CreateModel(
            name='CastImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='events/cast')),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cast_images', to='EventStation.eventdetails')),
            ],
            options={
                'db_table': 'eventstation_castimages',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='EventStation.eventdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserprofileStation.userprofile')),
            ],
            options={
                'db_table': 'eventstation_registration',
                'unique_together': {('event', 'user')},
            },
        ),
    ]
