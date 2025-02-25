# Generated by Django 3.2.12 on 2024-07-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('message', models.TextField()),
            ],
        ),
    ]
