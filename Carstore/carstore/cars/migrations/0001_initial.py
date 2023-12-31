# Generated by Django 4.2.3 on 2023-07-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('car_model', models.CharField(max_length=255)),
                ('engine', models.CharField(max_length=255)),
                ('fuel_type', models.CharField(max_length=255)),
                ('interior_color', models.CharField(max_length=255)),
            ],
        ),
    ]
