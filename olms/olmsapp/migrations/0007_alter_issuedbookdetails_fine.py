# Generated by Django 5.1.1 on 2024-11-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olmsapp', '0006_alter_issuedbookdetails_fine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbookdetails',
            name='fine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]