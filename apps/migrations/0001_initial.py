# Generated by Django 4.0.6 on 2022-07-07 18:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('sex', models.IntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]