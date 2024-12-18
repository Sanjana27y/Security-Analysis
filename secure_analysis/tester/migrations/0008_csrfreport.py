# Generated by Django 5.0 on 2023-12-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0007_xssreport_field_xssreport_location_xssreport_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSRFReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('is_vulnerable', models.BooleanField(default=False)),
            ],
        ),
    ]
