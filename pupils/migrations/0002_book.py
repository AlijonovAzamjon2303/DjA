# Generated by Django 5.2.1 on 2025-05-15 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pupils.pupil')),
            ],
        ),
    ]
