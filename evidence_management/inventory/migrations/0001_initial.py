# Generated by Django 5.1.5 on 2025-01-29 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=100)),
                ('hovj', models.CharField(max_length=255)),
                ('team', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('collected_on', models.DateField()),
                ('added_by', models.CharField(max_length=255)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidences', to='inventory.case')),
            ],
        ),
    ]
