# Generated by Django 5.0 on 2023-12-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0006_xssreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='xssreport',
            name='field',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='xssreport',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='xssreport',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]