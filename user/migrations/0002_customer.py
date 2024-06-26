# Generated by Django 5.0.4 on 2024-05-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
