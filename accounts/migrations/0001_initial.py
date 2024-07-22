# Generated by Django 3.2.25 on 2024-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.TextField(max_length=200)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('user_id', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
