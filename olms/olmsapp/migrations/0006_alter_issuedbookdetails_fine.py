# Generated by Django 5.1.1 on 2024-11-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olmsapp', '0005_alter_issuedbookdetails_fine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbookdetails',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
