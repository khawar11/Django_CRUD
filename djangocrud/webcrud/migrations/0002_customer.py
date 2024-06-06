# Generated by Django 5.0.6 on 2024-06-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('acquired_on', models.DateField()),
                ('customer_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
