# Generated by Django 5.0.4 on 2024-04-21 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('species', models.CharField(max_length=10)),
                ('url_image', models.CharField(max_length=500)),
                ('state', models.IntegerField()),
                ('shelter', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contacts_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('cell_phone', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=500)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_friendly.animal')),
            ],
        ),
    ]